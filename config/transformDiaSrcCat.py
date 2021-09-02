# Config override for lsst.ap.association.TransformDiaSourceCatalogTask
# Templates are deepCoadds

config.connections.coaddName = "deep"

# TODO: redundant connection definitions workaround for DM-30210
config.connections.diaSourceSchema = "deepDiff_diaSrc_schema"
config.connections.diaSourceCat = "deepDiff_diaSrc"
config.connections.diffIm = "deepDiff_differenceExp"
config.connections.diaSourceTable = "deepDiff_diaSrcTable"
# TODO: end DM-30210 workaround
