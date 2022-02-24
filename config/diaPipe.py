# Config override for lsst.ap.association.DiaPipelineTask
# Templates are deepCoadds

config.connections.coaddName = "deep"
config.doSolarSystemAssociation = True

# TODO: redundant connection definitions workaround for DM-30210
config.connections.diaSourceTable = "deepDiff_diaSrcTable"
config.connections.diffIm = "deepDiff_differenceExp"
config.connections.warpedExposure = "deepDiff_warpedExp"
config.connections.associatedDiaSources = "deepDiff_assocDiaSrc"
# TODO: end DM-30210 workaround
