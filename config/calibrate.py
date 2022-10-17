# Config override for lsst.pipe.tasks.calibrate.CalibrateTask

import warnings

warnings.warn('ap_verify_hits2015 is deprecated; it will be removed from the Rubin Observatory '
              'Science Pipelines after release 25.0.0', category=FutureWarning)

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
