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

"""Script for copying templates appropriate for these fields.

The datasets can be from any source, including the generate_templates_gen3.sh
script in this directory.

Example:
$ python import_templates_gen3.py -t "u/me/DM-123456-template"
imports deep templates from u/me/DM-123456-template in /repo/main to
templates/deep in this dataset's preloaded repo. See
generate_templates_gen3.sh -h for more options.
"""

import argparse
import logging
import os
import sys
import tempfile

import lsst.log
import lsst.skymap
from lsst.daf.butler import Butler, CollectionType


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
lsst.log.configure_pylog_MDC("DEBUG", MDC_class=None)


########################################
# Command-line options

def _make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="src_dir", default="/repo/main",
                        help="Repo to import from, defaults to '/repo/main'.")
    parser.add_argument("-t", dest="src_collection", required=True,
                        help="Template collection to import from.")
    return parser


args = _make_parser().parse_args()


########################################
# Export/Import

TEMPLATE_TYPE = "deep"
TEMPLATE_NAME = TEMPLATE_TYPE + "Coadd"
TEMPLATE_COLLECT = "templates/" + TEMPLATE_TYPE
DATASET_REPO = os.path.join(os.environ["AP_VERIFY_HITS2015_DIR"], "preloaded")


def _export(butler, export_file):
    """Export the files to be copied.

    Parameters
    ----------
    butler : `lsst.daf.butler.Butler`
        A Butler pointing to the repository and collection(s) to be
        exported from.
    export_file : `str`
        A path pointing to a file to contain the export results.

    Returns
    -------
    runs : iterable [`str`]
        The names of the runs containing exported templates.
    """
    skymaps = butler.registry.queryDataIds("skymap", datasets=TEMPLATE_NAME, collections=butler.collections)
    skymap_query = f"skymap IN ({', '.join(repr(id['skymap']) for id in skymaps)})"
    with butler.export(filename=export_file, transfer=None) as contents:
        contents.saveDatasets(
            butler.registry.queryDatasets(
                "skyMap", collections=lsst.skymap.BaseSkyMap.SKYMAP_RUN_COLLECTION_NAME,
                findFirst=True, where=skymap_query),
            elements=set())
        templates = butler.registry.queryDatasets(TEMPLATE_NAME, collections=butler.collections,
                                                  findFirst=True)
        contents.saveDatasets(templates)
        # Do not save butler.collections -- if they are RUN collections, it's
        # redundant; if they are CHAINED, they likely contain content that
        # isn't being transferred.
        return {t.run for t in templates}


def _import(butler, export_file, base_dir):
    """Import the exported files.

    Parameters
    ----------
    butler : `lsst.daf.butler.Butler`
        A Butler pointing to the dataset repository.
    export_file : `str`
        A path pointing to a file containing the export results.
    base_dir : `str`
        The base directory for the file locations in ``export_file``.
    """
    butler.import_(directory=base_dir, filename=export_file, transfer="copy")


with tempfile.NamedTemporaryFile(suffix=".yaml") as export_file:
    src = Butler(args.src_dir, collections=args.src_collection, writeable=False)
    runs = _export(src, export_file.name)
    dest = Butler(DATASET_REPO, writeable=True)
    _import(dest, export_file.name, args.src_dir)
    dest.registry.registerCollection(TEMPLATE_COLLECT, CollectionType.CHAINED)
    dest.registry.setCollectionChain(TEMPLATE_COLLECT, runs)

logging.info(f"Templates stored in {DATASET_REPO}:{TEMPLATE_COLLECT}.")
