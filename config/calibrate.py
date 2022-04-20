# Config override for lsst.pipe.tasks.calibrate.CalibrateTask

# Use gaia for astrometry (phot_g_mean for everything, as that is the broadest
# band with the most depth)
config.connections.astromRefCat = "gaia"
config.astromRefObjLoader.ref_dataset_name = config.connections.astromRefCat
config.astromRefObjLoader.anyFilterMapsToThis = "phot_g_mean"

# Use panstarrs for photometry (grizy filters)
config.connections.photoRefCat = "panstarrs"
config.photoRefObjLoader.ref_dataset_name = config.connections.photoRefCat
config.photoRefObjLoader.filterMap = {
    "u": "g",
    "VR": "g"}
