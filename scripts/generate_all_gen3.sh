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

# Script for regenerating a complete Gen 3 repository in preloaded/.
# It takes roughly 34 hours to run on lsst-devl.
#
# Example:
# $ nohup generate_all_gen3.sh -c "u/me/DM-123456" &
# fills this dataset, using collections prefixed by u/me/DM-123456 in
# /repo/main as a staging area. See generate_all_gen3.sh -h for more options.


# Abort script on any error
set -e

SCRIPT_DIR="$( dirname -- "${BASH_SOURCE[0]}" )"
DATASET_REPO="${AP_VERIFY_HITS2015_DIR:?'dataset is not set up'}/preloaded/"


########################################
# Command-line options

print_error() {
    >&2 echo "$@"
}

usage() {
    print_error
    print_error "Usage: $0 [-b BUTLER_REPO] -c ROOT_COLLECTION [-h]"
    print_error
    print_error "Specific options:"
    print_error "   -b          Butler repo URI, defaults to /repo/main"
    print_error "   -c          unique base collection name for processing; will also appear in final repo"
    print_error "   -h          show this message"
    exit 1
}

parse_args() {
    while getopts "b:c:h" option $@; do
        case "$option" in
            b)  SCRATCH_REPO="$OPTARG";;
            c)  COLLECT_ROOT="$OPTARG";;
            h)  usage;;
            *)  usage;;
        esac
    done
    if [[ -z "${SCRATCH_REPO}" ]]; then
        SCRATCH_REPO="/repo/main"
    fi
    if [[ -z "${COLLECT_ROOT}" ]]; then
        print_error "$0: mandatory argument -- c"
        usage
        exit 1
    fi
}
parse_args $@


CALIB_COLLECTION_SCI="${COLLECT_ROOT}-calib-science"
CALIB_COLLECTION_TMP="${COLLECT_ROOT}-calib-template"
TEMPLATE_COLLECTION="${COLLECT_ROOT}-template"
REPO_COLLECTION="refcats"


########################################
# Prepare calibs

"${SCRIPT_DIR}/generate_calibs_gen3_science.sh" -b ${SCRATCH_REPO} -c "${CALIB_COLLECTION_SCI}"


########################################
# Prepare templates

"${SCRIPT_DIR}/generate_calibs_gen3_template.sh" -b ${SCRATCH_REPO} -c "${CALIB_COLLECTION_TMP}"
"${SCRIPT_DIR}/generate_templates_gen3.sh" -b ${SCRATCH_REPO} -c "${CALIB_COLLECTION_TMP}-calib" \
    -o "${TEMPLATE_COLLECTION}"


########################################
# Repository creation

"${SCRIPT_DIR}/make_preloaded.sh"


########################################
# Import calibs, templates, and refcats

"${SCRIPT_DIR}/import_calibs_gen3.sh" -b ${SCRATCH_REPO} -c "${CALIB_COLLECTION_SCI}-calib"
python "${SCRIPT_DIR}/import_templates_gen3.py" -b ${SCRATCH_REPO} -t "${TEMPLATE_COLLECTION}"
python "${SCRIPT_DIR}/generate_refcats_gen3.py" -b ${SCRATCH_REPO} -i "${REPO_COLLECTION}"


########################################
# Final clean-up

butler collection-chain "${DATASET_REPO}" refcats refcats/imported
butler collection-chain "${DATASET_REPO}" DECam/defaults templates/deep skymaps DECam/calib refcats
python "${SCRIPT_DIR}/make_preloaded_export.py" --dataset ap_verify_hits2015

echo "Gen 3 preloaded repository complete."
echo "All preloaded data products are accessible through the DECam/defaults collection."
