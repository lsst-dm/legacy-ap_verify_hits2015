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

# Script for importing certified calibs from a work repository.
#
# Example:
# $ import_calibs_gen3 -c "u/me/DM-123456-calib"
# imports certified calibs from u/me/DM-123456-calib in /repo/main to
# DECam/calib in this dataset's preloaded repo. See
# import_calibs_gen3.sh -h for more options.


# Abort script on any error
set -e


########################################
# Command-line options

print_error() {
    >&2 echo "$@"
}

usage() {
    print_error
    print_error "Usage: $0 [-b BUTLER_REPO] -c CALIB_COLLECTION [-h]"
    print_error
    print_error "Specific options:"
    print_error "   -b          Source Butler repo URI, defaults to /repo/main"
    print_error "   -c          Source calib collection name"
    print_error "   -h          show this message"
    exit 1
}

parse_args() {
    while getopts "b:c:h" option $@; do
        case "$option" in
            b)  SRC_REPO="$OPTARG";;
            c)  CALIB_SRC="$OPTARG";;
            h)  usage;;
            *)  usage;;
        esac
    done
    if [[ -z "${SRC_REPO}" ]]; then
        SRC_REPO="/repo/main"
    fi
    if [[ -z "${CALIB_SRC}" ]]; then
        print_error "$0: mandatory argument -- c"
        usage
        exit 1
    fi
}
parse_args "$@"


########################################
# Export/Import

CALIB_COLLECT="DECam/calib"
DATASET_REPO="${AP_VERIFY_HITS2015_DIR:?'dataset is not set up'}/preloaded/"
STORAGE_DIR="${PWD}/tmp_import"

if [[ -d "$STORAGE_DIR" ]]; then
    # Left over from a failed run
    rm -rf "$STORAGE_DIR"
fi

echo "Transferring calibs..."
butler export-calibs "$SRC_REPO" "$STORAGE_DIR" "$CALIB_SRC"
butler import "$DATASET_REPO" "$STORAGE_DIR" --transfer copy \
    --skip-dimensions instrument,detector,physical_filter
rm -rf "$STORAGE_DIR"

# Calibs were imported into another collection named $CALIB_SRC.
butler collection-chain "$DATASET_REPO" "$CALIB_COLLECT" "$CALIB_SRC" --mode prepend


########################################
# Final summary

echo "Calibs stored in ${DATASET_REPO}:${CALIB_COLLECT}"
