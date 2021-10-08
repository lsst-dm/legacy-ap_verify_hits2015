# Config override for lsst.pipe.tasks.imageDifference.ImageDifferenceTask
# Templates are deepCoadds assembled with the CompareWarp algorithm

# This file is only needed to provide the explicit "fakes_" connections names
# required by DM-30210. Once that issue is resolved, this file can be removed
# and the pipeline can use imageDifference.py plus a direct override
# of fakesType.

config.connections.fakesType = "fakes_"
config.connections.coaddName = "deep"
# These two lines can be removed once ImageDifference no longer supports Gen 2
config.coaddName = config.connections.coaddName
config.getTemplate.coaddName = config.connections.coaddName

# TODO: redundant connection definitions workaround for DM-30210
config.connections.exposure = "fakes_calexp"
config.connections.coaddExposures = "fakes_deepCoadd"
config.connections.dcrCoadds = "fakes_dcrCoadd"
config.connections.outputSchema = "fakes_deepDiff_diaSrc_schema"
config.connections.subtractedExposure = "fakes_deepDiff_differenceExp"
config.connections.scoreExposure = "fakes_deepDiff_scoreExp"
config.connections.warpedExposure = "fakes_deepDiff_warpedExp"
config.connections.matchedExposure = "fakes_deepDiff_matchedExp"
config.connections.diaSources = "fakes_deepDiff_diaSrc"
# TODO: end DM-30210 workaround
