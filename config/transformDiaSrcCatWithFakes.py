# Config override for lsst.ap.association.TransformDiaSourceCatalogTask
# Templates are deepCoadds

# This file is only needed to provide the explicit "fakes_" connections names
# required by DM-30210. Once that issue is resolved, this file can be removed
# and the pipeline can use transformDiaSrcCat.py plus a direct override
# of fakesType.

config.connections.fakesType = "fakes_"
config.connections.coaddName = "deep"

# TODO: redundant connection definitions workaround for DM-30210
config.connections.diaSourceSchema = "fakes_deepDiff_diaSrc_schema"
config.connections.diaSourceCat = "fakes_deepDiff_diaSrc"
config.connections.diffIm = "fakes_deepDiff_differenceExp"
config.connections.diaSourceTable = "fakes_deepDiff_diaSrcTable"
# TODO: end DM-30210 workaround
