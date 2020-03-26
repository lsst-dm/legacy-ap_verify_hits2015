# Config override for lsst.pipe.tasks.calibrate.CalibrateTask
from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask

# Use gaia for astrometry (phot_g_mean for everything, as that is the broadest
# band with the most depth)
# Use panstarrs for photometry (grizy filters)
for refObjLoader in (config.astromRefObjLoader,
                     config.photoRefObjLoader,):
    refObjLoader.retarget(LoadIndexedReferenceObjectsTask)
config.connections.astromRefCat = "gaia"
config.astromRefObjLoader.ref_dataset_name = config.connections.astromRefCat
config.astromRefObjLoader.filterMap = {
    "u": "phot_g_mean",
    "g": "phot_g_mean",
    "r": "phot_g_mean",
    "i": "phot_g_mean",
    "z": "phot_g_mean",
    "y": "phot_g_mean",
    "VR": "phot_g_mean"}
config.connections.photoRefCat = "panstarrs"
config.photoRefObjLoader.ref_dataset_name = config.connections.photoRefCat
config.photoRefObjLoader.filterMap = {
    "u": "g",
    "g": "g",
    "r": "r",
    "i": "i",
    "z": "z",
    "y": "y",
    "VR": "g"}
