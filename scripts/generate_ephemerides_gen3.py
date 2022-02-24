#!/usr/bin/env python
# This file is part of ap_verify_hits2015.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Script for downloading solar system object ephemerides for this dataset's
fields and observation times.

Running this script allows for updates to the ephemerides to be incorporated
into the dataset.
"""

import glob
import logging
import os
import subprocess
import sys
import tempfile

import lsst.log
import lsst.sphgeom
from lsst.daf.butler import Butler, FileDataset
import lsst.obs.base


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
lsst.log.configure_pylog_MDC("DEBUG", MDC_class=None)


# Avoid explicit references to dataset package to maximize portability.
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
PIPE_DIR = os.path.join(SCRIPT_DIR, "..", "pipelines")
RAW_DIR = os.path.join(SCRIPT_DIR, "..", "raw")
RAW_RUN = "raw"
EPHEM_DATASET = "visitSsObjects"
DEST_DIR = os.path.join(SCRIPT_DIR, "..", "preloaded")
DEST_RUN = "sso/cached"


########################################
# Set up temp repository

def _get_instruments(repo_dir):
    """Find all instruments supported by a repository.

    Parameters
    ----------
    repo_dir : `str`
        The repository to search for instruments.

    Returns
    -------
    instruments : `list` [`lsst.obs.base.Instrument`]
    """
    registry = Butler(repo_dir, writeable=False).registry
    ids = registry.queryDataIds("instrument")
    return [lsst.obs.base.Instrument.fromName(id["instrument"], registry) for id in ids]


def _make_repo_with_instruments(repo_dir, instruments):
    """Create a repository and populate it with instrument registrations from
    an existing repository.

    Parameters
    ----------
    repo_dir : `str`
        The directory in which to create the new repository.
    instrument : iterable [`lsst.obs.base.Instrument`]
        The instruments to register in the new repository.

    Returns
    -------
    butler : `lsst.daf.butler.Butler`
        A writeable Butler to the new repo.
    """
    config = Butler.makeRepo(repo_dir)
    repo = Butler(config, writeable=True)
    for instrument in instruments:
        instrument.register(repo.registry)
    return repo


########################################
# Ingest raws (needed for visitinfo)

def _ingest_raws(repo, raw_dir, run):
    """Ingest this dataset's raws into a specific repo.

    Parameters
    ---------
    repo : `lsst.daf.butler.Butler`
        A writeable Butler for the repository to ingest into.
    raw_dir : `str`
        The directory containing raw files.
    run : `str`
        The name of the run into which to import the raws.
    """
    raws = glob.glob(os.path.join(raw_dir, '**', '*.fits.fz'), recursive=True)
    # explicit config workaround for DM-971
    ingester = lsst.obs.base.RawIngestTask(butler=repo, config=lsst.obs.base.RawIngestConfig())
    ingester.run(raws, run=run)
    exposures = set(repo.registry.queryDataIds(["exposure"]))
    # explicit config workaround for DM-971
    definer = lsst.obs.base.DefineVisitsTask(butler=repo, config=lsst.obs.base.DefineVisitsConfig())
    definer.run(exposures)


########################################
# Download ephemerides

def _get_ephem(repo_dir, raw_collection, ephem_collection):
    """Run the task for downloading ephemerides.

    Parameters
    ----------
    repo_dir : `str`
        The repository on which to run the task.
    raw_collection : `str`
        The collection containing input raws.
    ephem_collection : `str`
        The collection into which to generate ephemerides.

    Raises
    ------
    RuntimeError
        Raised on any pipeline failure.
    """
    pipeline_file = os.path.join(PIPE_DIR, "Ephemerides.yaml")
    pipeline_args = ["pipetask", "run",
                     "--butler-config", repo_dir,
                     "--pipeline", pipeline_file,
                     "--input", raw_collection,
                     "--output-run", ephem_collection,
                     "--processes", "12",
                     "--register-dataset-types",
                     ]
    results = subprocess.run(pipeline_args, capture_output=False, shell=False, check=False)
    if results.returncode:
        raise RuntimeError("Pipeline failed to run; see log for details.")


########################################
# Import/export

def _transfer_ephems(ephem_type, src_repo, src_dir, run, dest_repo):
    """Copy ephemerides between two repositories.

    Parameters
    ----------
    ephem_type : `str`
        The dataset type of the ephemerides.
    src_repo : `lsst.daf.butler.Butler`
        The repository from which to copy the datasets.
    src_dir : `str`
        The location of ``src_repo``.
    run : `str`
        The name of the run containing the ephemerides in both ``src_repo``
        and ``dest_repo``.
    dest_repo : `lsst.daf.butler.Butler`
        The repository to which to copy the datasets.
    """
    # Need to transfer visit definitions as well; Butler.export is the easiest
    # way to do this.
    with tempfile.NamedTemporaryFile(suffix=".yaml") as export_file:
        with src_repo.export(filename=export_file.name, transfer=None) as contents:
            contents.saveDatasets(src_repo.registry.queryDatasets(ephem_type, collections=run),
                                  elements=["visit"])
            # Because of how the temp repo was constructed, there should not be
            # any visit/exposure records other than those needed to support the
            # ephemerides datasets.
            contents.saveDimensionData("visit_system",
                                       src_repo.registry.queryDimensionRecords("visit_system"))
            contents.saveDimensionData("visit",
                                       src_repo.registry.queryDimensionRecords("visit"))
            contents.saveDimensionData("exposure",
                                       src_repo.registry.queryDimensionRecords("exposure"))
            contents.saveDimensionData("visit_definition",
                                       src_repo.registry.queryDimensionRecords("visit_definition"))
            contents.saveDimensionData("visit_detector_region",
                                       src_repo.registry.queryDimensionRecords("visit_detector_region"))
            # runs included automatically by saveDatasets
        dest_repo.import_(directory=src_dir, filename=export_file.name, transfer="copy")


########################################
# Put everything together

logging.info("Creating temporary repository...")
with tempfile.TemporaryDirectory() as workspace:
    temp_repo = _make_repo_with_instruments(workspace, _get_instruments(DEST_DIR))
    logging.info("Ingesting raws...")
    _ingest_raws(temp_repo, RAW_DIR, RAW_RUN)
    logging.info("Downloading ephemerides...")
    _get_ephem(workspace, RAW_RUN, DEST_RUN)
    temp_repo.registry.refresh()    # Pipeline added dataset types
    preloaded = Butler(DEST_DIR, writeable=True)
    logging.info("Transferring ephemerides to dataset...")
    _transfer_ephems(EPHEM_DATASET, temp_repo, workspace, DEST_RUN, preloaded)

logging.info("Solar system catalogs copied to %s:%s", DEST_DIR, DEST_RUN)
