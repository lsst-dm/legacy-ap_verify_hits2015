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

# Common code for generate_calibs_gen3_*.
# This script is intended to be included by other scripts, rather than
# called directly.

# Abort script on any error
set -e

########################################
# Variable management

# from https://stackoverflow.com/questions/1527049/how-can-i-join-elements-of-an-array-in-bash
join_by() { local IFS="$1"; shift; echo "$*"; }


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
    print_error "   -c          unique base collection name"
    print_error "   -h          show this message"
    exit 1
}

parse_args() {
    while getopts "b:c:h" option $@; do
        case "$option" in
            b)  BUTLER_REPO="$OPTARG";;
            c)  COLLECT_ROOT="$OPTARG";;
            h)  usage;;
            *)  usage;;
        esac
    done
    if [[ -z "${BUTLER_REPO}" ]]; then
        BUTLER_REPO="/repo/main"
    fi
    if [[ -z "${COLLECT_ROOT}" ]]; then
        print_error "$0: mandatory argument -- c"
        usage
        exit 1
    fi
}


########################################
# Prepare crosstalk sources (overscan subtraction)

# TODO: overscan.fitType override may be included in cp_pipe on DM-30651

do_crosstalk() {
    local repo="$1"       # Butler URI
    local collect="$2"    # Partial collection name
    local exposures="$3"  # Comma-delimited list of exposure IDs
    pipetask run -j 12 -d "exposure IN ($exposures) AND instrument='DECam'" \
        -b ${repo} -i DECam/defaults -o ${collect}-crosstalk-sources \
        -p $CP_PIPE_DIR/pipelines/DarkEnergyCamera/RunIsrForCrosstalkSources.yaml \
        -c overscan:overscan.fitType='MEDIAN_PER_ROW'
}

########################################
# Build and certify bias frames

# TODO: overscan.fitType override may be included in cp_pipe on DM-30651

do_bias() {
    local repo="$1"                    # Butler URI
    local collect="$2"                 # Partial collection name
    # Associative array hack from https://stackoverflow.com/questions/4069188/
    # Arrays must be passed as strings from calling declare -p.
    # Associative array of coma-delimited list of exposure IDs, keyed by 1-word "date"
    eval "local -A exposures=${3#*=}"
    # Associative array of "--begin-date --end-date", with same keys as $exposures
    eval "local -A validities=${4#*=}"

    for date in ${!exposures[*]}; do
        pipetask run -j 12 -d "exposure IN (${exposures[${date}]}) AND instrument='DECam'" \
            -b ${repo} -i DECam/defaults -o ${collect}-bias-construction-${date} \
            -p $CP_PIPE_DIR/pipelines/cpBias.yaml -c isr:overscan.fitType='MEDIAN_PER_ROW'
        butler certify-calibrations ${repo} ${collect}-bias-construction-${date} \
            ${collect}-calib bias ${validities[${date}]}
    done
}

########################################
# Build and certify flat frames

# TODO: cpFlatNorm:level override may be included in cp_pipe on DM-30651

do_flat() {
    local repo="$1"                    # Butler URI
    local collect="$2"                 # Partial collection name
    # Associative array hack from https://stackoverflow.com/questions/4069188/
    # Arrays must be passed as strings from calling declare -p.
    # Associative array of coma-delimited list of exposure IDs, keyed by 1-word "date"
    eval "local -A exposures=${3#*=}"
    # Associative array of "--begin-date --end-date", with same keys as $exposures
    eval "local -A validities=${4#*=}"

    for date in ${!exposures[*]}; do
        pipetask run -j 12 -d "exposure IN (${exposures[${date}]}) AND instrument='DECam'" \
            -b ${repo} -i DECam/defaults,${collect}-calib,${collect}-crosstalk-sources \
            -o ${collect}-flat-construction-${date} \
            -p $CP_PIPE_DIR/pipelines/DarkEnergyCamera/cpFlat.yaml -c cpFlatNorm:level='AMP'
        butler certify-calibrations ${repo} ${collect}-flat-construction-${date} \
            ${collect}-calib flat ${validities[${date}]}
    done
}
