# Config override for lsst.pipe.tasks.imageDifference.ImageDifferenceTask
# Templates are deepCoadds assembled with the CompareWarp algorithm

config.connections.coaddName = "deep"
# These two lines can be removed once ImageDifference no longer supports Gen 2
config.coaddName = config.connections.coaddName
config.getTemplate.coaddName = config.connections.coaddName

# TODO: redundant connection definitions workaround for DM-30210
config.connections.exposure = "calexp"
config.connections.coaddExposures = "deepCoadd"
config.connections.dcrCoadds = "dcrCoadd"
config.connections.outputSchema = "deepDiff_diaSrc_schema"
config.connections.subtractedExposure = "deepDiff_differenceExp"
config.connections.scoreExposure = "deepDiff_scoreExp"
config.connections.warpedExposure = "deepDiff_warpedExp"
config.connections.matchedExposure = "deepDiff_matchedExp"
config.connections.diaSources = "deepDiff_diaSrc"
# TODO: end DM-30210 workaround
