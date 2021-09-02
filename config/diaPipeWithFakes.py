# Config override for lsst.ap.association.DiaPipelineTask
# Templates are deepCoadds

# This file is only needed to provide the explicit "fakes_" connections names
# required by DM-30210. Once that issue is resolved, this file can be removed
# and the pipeline can use diaPipe.py plus a direct override of fakesType.

config.connections.fakesType = "fakes_"
config.connections.coaddName = "deep"

# TODO: redundant connection definitions workaround for DM-30210
config.connections.diaSourceTable = "fakes_deepDiff_diaSrcTable"
config.connections.diffIm = "fakes_deepDiff_differenceExp"
config.connections.warpedExposure = "fakes_deepDiff_warpedExp"
config.connections.associatedDiaSources = "fakes_deepDiff_assocDiaSrc"
# TODO: end DM-30210 workaround
