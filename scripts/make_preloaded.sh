#!/bin/bash
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

# Script for generating a fresh Gen 3 repository in preloaded/. The previous
# copy is removed.


# Abort script on any error
set -e


########################################
# Repository creation

REPO_DIR="${AP_VERIFY_HITS2015_DIR:?'dataset is not set up'}/preloaded/"

rm -rf "$REPO_DIR"
butler create "$REPO_DIR" --standalone
butler register-instrument "$REPO_DIR" lsst.obs.decam.DarkEnergyCamera
echo "Created fresh repo in ${REPO_DIR}."


########################################
# Minimal contents

STD_CALIB="DECam/calib"
CURATED_CALIB="${STD_CALIB}/curated"

# TODO: this step may become unneccessary after DM-32975.
butler write-curated-calibrations "$REPO_DIR" lsst.obs.decam.DarkEnergyCamera \
    --collection "$CURATED_CALIB"
butler collection-chain "$REPO_DIR" "$STD_CALIB" "$CURATED_CALIB"
echo "Added curated calibrations to ${REPO_DIR}."
