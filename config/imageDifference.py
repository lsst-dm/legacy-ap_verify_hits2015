# Config override for lsst.pipe.tasks.imageDifference.ImageDifferenceTask
# Templates are deepCoadds assembled with the CompareWarp algorithm
config.coaddName = "deep"
config.getTemplate.coaddName = config.coaddName
config.getTemplate.warpType = "direct"
