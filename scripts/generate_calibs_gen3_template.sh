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

# Script for automatically generating template calibs for this dataset. It
# takes roughly 4 hours to run on lsst-devl.
# This script should be run before generating templates in order to
# self-consistently use all pipeline improvements.
#
# Example:
# $ nohup generate_calibs_gen3_template.sh -c "u/me/DM-123456" &
# produces certified calibs in /repo/main in the u/me/DM-123456-calib
# collection. See generate_calibs_gen3_template.sh -h for more options.


# Common definitions
SCRIPT_DIR="$( dirname -- "${BASH_SOURCE[0]}" )"
source "${SCRIPT_DIR}/generate_calibs_gen3.sh"


########################################
# Raw calibs to process

# Syntax matters -- use
#     https://pipelines.lsst.io/v/daily/modules/lsst.daf.butler/queries.html#dimension-expressions
#     syntax, with no trailing comma.

declare -A EXPOSURES_BIAS
EXPOSURES_BIAS[20140228]='288902, 288903, 288904, 288905, 288906, 288907, 288908, 288909, 288910,
                          288911, 288912'
EXPOSURES_BIAS[20140301]='289119, 289120, 289121, 289122, 289123, 289124, 289125, 289126, 289127,
                          289128, 289129'
EXPOSURES_BIAS[20140302]='289328, 289329, 289330, 289331, 289332, 289333, 289334, 289335, 289336,
                          289337, 289338'
EXPOSURES_BIAS[20140303]='289532, 289533, 289534, 289535, 289536, 289537, 289538, 289539, 289540,
                          289541, 289542'
EXPOSURES_BIAS[20140304]='289742, 289743, 289744, 289745, 289746, 289747, 289748, 289749, 289750,
                          289751, 289752'

declare -A VALIDITIES_BIAS
VALIDITIES_BIAS[20140228]='--begin-date 2014-02-15T00:00:00 --end-date 2014-02-28T23:59:59'
VALIDITIES_BIAS[20140301]='--begin-date 2014-03-01T00:00:00 --end-date 2014-03-01T23:59:59'
VALIDITIES_BIAS[20140302]='--begin-date 2014-03-02T00:00:00 --end-date 2014-03-02T23:59:59'
VALIDITIES_BIAS[20140303]='--begin-date 2014-03-03T00:00:00 --end-date 2014-03-03T23:59:59'
VALIDITIES_BIAS[20140304]='--begin-date 2014-03-04T00:00:00 --end-date 2014-03-15T23:59:59'

declare -A EXPOSURES_FLAT_g_c0001
EXPOSURES_FLAT_g_c0001[20140228]='288847, 288848, 288849, 288850, 288851, 288852, 288853, 288854,
                                  288855, 288856, 288857'
EXPOSURES_FLAT_g_c0001[20140301]='289130, 289131, 289132, 289133, 289134, 289135, 289136, 289137,
                                  289138, 289139, 289140'
EXPOSURES_FLAT_g_c0001[20140302]='289339, 289340, 289341, 289342, 289343, 289344, 289345, 289346,
                                  289347, 289348, 289349'
EXPOSURES_FLAT_g_c0001[20140303]='289543, 289544, 289545, 289546, 289547, 289548, 289549, 289550,
                                  289551, 289552, 289553'
EXPOSURES_FLAT_g_c0001[20140304]='289753, 289754, 289755, 289756, 289757, 289758, 289759, 289760,
                                  289761, 289762, 289763'

declare -A VALIDITIES_FLAT_g_c0001
VALIDITIES_FLAT_g_c0001[20140228]='--begin-date 2014-02-15T00:00:00 --end-date 2014-02-28T23:59:59'
VALIDITIES_FLAT_g_c0001[20140301]='--begin-date 2014-03-01T00:00:00 --end-date 2014-03-01T23:59:59'
VALIDITIES_FLAT_g_c0001[20140302]='--begin-date 2014-03-02T00:00:00 --end-date 2014-03-02T23:59:59'
VALIDITIES_FLAT_g_c0001[20140303]='--begin-date 2014-03-03T00:00:00 --end-date 2014-03-03T23:59:59'
VALIDITIES_FLAT_g_c0001[20140304]='--begin-date 2014-03-04T00:00:00 --end-date 2014-03-15T23:59:59'

EXPOSURES_CROSSTALK=$(join_by , "${EXPOSURES_FLAT_g_c0001[@]}")


########################################
# Command-line options

parse_args "$@"


########################################
# Generate calibs

do_crosstalk $BUTLER_REPO $COLLECT_ROOT "$EXPOSURES_CROSSTALK"

# Associative array hack from https://stackoverflow.com/questions/4069188/
do_bias $BUTLER_REPO $COLLECT_ROOT "$(declare -p EXPOSURES_BIAS)" "$(declare -p VALIDITIES_BIAS)"
do_flat $BUTLER_REPO $COLLECT_ROOT \
    "$(declare -p EXPOSURES_FLAT_g_c0001)" "$(declare -p VALIDITIES_FLAT_g_c0001)"


########################################
# Final summary

echo "Biases and flats stored in ${BUTLER_REPO}:${COLLECT_ROOT}-calib"
