# Config override for lsst.ap.pipe.ApPipeTask
import os.path
from lsst.utils import getPackageDir
from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask

decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')

config.ccdProcessor.load(os.path.join(decamConfigDir, "processCcd.py"))

# Use gaia for astrometry (phot_g_mean for everything, as that is the broadest
# band with the most depth)
# Use panstarrs for photometry (grizy filters)
for refObjLoader in (config.ccdProcessor.calibrate.astromRefObjLoader,
                     config.ccdProcessor.calibrate.photoRefObjLoader,):
    refObjLoader.retarget(LoadIndexedReferenceObjectsTask)
config.ccdProcessor.calibrate.connections.astromRefCat = "gaia"
config.ccdProcessor.calibrate.astromRefObjLoader.ref_dataset_name = \
    config.ccdProcessor.calibrate.connections.astromRefCat
config.ccdProcessor.calibrate.astromRefObjLoader.filterMap = {
    "u": "phot_g_mean",
    "g": "phot_g_mean",
    "r": "phot_g_mean",
    "i": "phot_g_mean",
    "z": "phot_g_mean",
    "y": "phot_g_mean",
    "VR": "phot_g_mean"}
config.ccdProcessor.calibrate.connections.photoRefCat = "panstarrs"
config.ccdProcessor.calibrate.photoRefObjLoader.ref_dataset_name = \
    config.ccdProcessor.calibrate.connections.photoRefCat
config.ccdProcessor.calibrate.photoRefObjLoader.filterMap = {
    "u": "g",
    "g": "g",
    "r": "r",
    "i": "i",
    "z": "z",
    "y": "y",
    "VR": "g"}

# Templates are deepCoadds assembled with the CompareWarp algorithm
config.differencer.coaddName = "deep"
config.differencer.getTemplate.coaddName = config.differencer.coaddName
config.differencer.getTemplate.warpType = "direct"

