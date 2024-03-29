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

# Script for automatically generating calibs for this dataset. It takes roughly
# 6 hours to run on lsst-devl.
# Running this script allows for calibs to incorporate pipeline improvements.
# It makes no attempt to update the set of input exposures or their validity
# ranges; they are hard-coded into the file.
#
# Example:
# $ nohup generate_calibs_gen3_science.sh -c "u/me/DM-123456" &
# produces certified calibs in /repo/main in the u/me/DM-123456-calib
# collection. See generate_calibs_gen3_science.sh -h for more options.


# Common definitions
SCRIPT_DIR="$( dirname -- "${BASH_SOURCE[0]}" )"
source "${SCRIPT_DIR}/generate_calibs_gen3.sh"


########################################
# Raw calibs to process

# Syntax matters -- use
#     https://pipelines.lsst.io/v/daily/modules/lsst.daf.butler/queries.html#dimension-expressions
#     syntax, with no trailing comma.

declare -A EXPOSURES_BIAS
EXPOSURES_BIAS[20150216]='410714, 410715, 410716, 410717, 410718, 410719, 410720, 410721, 410722,
                          410723, 410724'
EXPOSURES_BIAS[20150217]='411102, 411103, 411104, 411105, 411106, 411107, 411108, 411109, 411110,
                          411111, 411112'
EXPOSURES_BIAS[20150218]='411502, 411503, 411504, 411505, 411506, 411507, 411508, 411509, 411510,
                          411511, 411512'
EXPOSURES_BIAS[20150219]='411904, 411905, 411906, 411907, 411908, 411909, 411910, 411911, 411912,
                          411913, 411914'
EXPOSURES_BIAS[20150220]='412096, 412097, 412098, 412099, 412100, 412101, 412102, 412103, 412104,
                          412105, 412106'
EXPOSURES_BIAS[20150221]='412355, 412356, 412357, 412358, 412359, 412360, 412361, 412362, 412363,
                          412364, 412365'
EXPOSURES_BIAS[20150223]='413448, 413449, 413450, 413451, 413452, 413453, 413454, 413455, 413456,
                          413457, 413458'
EXPOSURES_BIAS[20150226]='415136, 415137, 415138, 415139, 415140, 415141, 415142, 415143, 415144,
                          415145, 415146'
EXPOSURES_BIAS[20150313]='421350, 421351, 421352, 421353, 421354, 421355, 421356, 421357, 421358,
                          421359, 421360'

declare -A VALIDITIES_BIAS
VALIDITIES_BIAS[20150216]='--begin-date 2015-02-01T00:00:00 --end-date 2015-02-16T23:59:59'
VALIDITIES_BIAS[20150217]='--begin-date 2015-02-17T00:00:00 --end-date 2015-02-17T23:59:59'
VALIDITIES_BIAS[20150218]='--begin-date 2015-02-18T00:00:00 --end-date 2015-02-18T23:59:59'
VALIDITIES_BIAS[20150219]='--begin-date 2015-02-19T00:00:00 --end-date 2015-02-19T23:59:59'
VALIDITIES_BIAS[20150220]='--begin-date 2015-02-20T00:00:00 --end-date 2015-02-20T23:59:59'
VALIDITIES_BIAS[20150221]='--begin-date 2015-02-21T00:00:00 --end-date 2015-02-22T23:59:59'
VALIDITIES_BIAS[20150223]='--begin-date 2015-02-23T00:00:00 --end-date 2015-02-24T23:59:59'
VALIDITIES_BIAS[20150226]='--begin-date 2015-02-25T00:00:00 --end-date 2015-03-05T23:59:59'
VALIDITIES_BIAS[20150313]='--begin-date 2015-03-06T00:00:00 --end-date 2015-03-15T23:59:59'

declare -A EXPOSURES_FLAT_g_c0001
EXPOSURES_FLAT_g_c0001[20150216]='410790, 410791, 410792, 410793, 410794, 410795, 410796, 410797,
                                  410798, 410799, 410800'
EXPOSURES_FLAT_g_c0001[20150217]='411178, 411179, 411180, 411181, 411182, 411183, 411184, 411185,
                                  411186, 411187, 411188'
EXPOSURES_FLAT_g_c0001[20150218]='411578, 411579, 411580, 411581, 411582, 411583, 411584, 411585,
                                  411586, 411587, 411588'
EXPOSURES_FLAT_g_c0001[20150219]='411980, 411981, 411982, 411983, 411984, 411985, 411986, 411987,
                                  411988, 411989, 411990'
EXPOSURES_FLAT_g_c0001[20150220]='412172, 412173, 412174, 412175, 412176, 412177, 412178, 412179,
                                  412180, 412181, 412182'
EXPOSURES_FLAT_g_c0001[20150221]='412431, 412432, 412433, 412434, 412435, 412436, 412437, 412438,
                                  412439, 412440, 412441'
EXPOSURES_FLAT_g_c0001[20150223]='413524, 413525, 413526, 413527, 413528, 413529, 413530, 413531,
                                  413532, 413533, 413534'
EXPOSURES_FLAT_g_c0001[20150226]='415212, 415213, 415214, 415215, 415216, 415217, 415218, 415219,
                                  415220, 415221, 415222'
EXPOSURES_FLAT_g_c0001[20150313]='421426, 421427, 421428, 421429, 421430, 421431, 421432, 421433,
                                  421434, 421435, 421436'

declare -A VALIDITIES_FLAT_g_c0001
VALIDITIES_FLAT_g_c0001[20150216]='--begin-date 2015-02-01T00:00:00 --end-date 2015-02-16T23:59:59'
VALIDITIES_FLAT_g_c0001[20150217]='--begin-date 2015-02-17T00:00:00 --end-date 2015-02-17T23:59:59'
VALIDITIES_FLAT_g_c0001[20150218]='--begin-date 2015-02-18T00:00:00 --end-date 2015-02-18T23:59:59'
VALIDITIES_FLAT_g_c0001[20150219]='--begin-date 2015-02-19T00:00:00 --end-date 2015-02-19T23:59:59'
VALIDITIES_FLAT_g_c0001[20150220]='--begin-date 2015-02-20T00:00:00 --end-date 2015-02-20T23:59:59'
VALIDITIES_FLAT_g_c0001[20150221]='--begin-date 2015-02-21T00:00:00 --end-date 2015-02-22T23:59:59'
VALIDITIES_FLAT_g_c0001[20150223]='--begin-date 2015-02-23T00:00:00 --end-date 2015-02-24T23:59:59'
VALIDITIES_FLAT_g_c0001[20150226]='--begin-date 2015-02-25T00:00:00 --end-date 2015-03-05T23:59:59'
VALIDITIES_FLAT_g_c0001[20150313]='--begin-date 2015-03-06T00:00:00 --end-date 2015-03-15T23:59:59'

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
