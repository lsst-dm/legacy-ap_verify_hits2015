# Config override for lsst.ap.pipe.ApPipeTask
import os.path
from lsst.utils import getPackageDir
from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask

decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')

# Use Community Pipeline calibration products instead of the defaults
config.ccdProcessor.load(os.path.join(decamConfigDir, "processCcdCpIsr.py"))

# Use gaia for astrometry (phot_g_mean_mag is only available DR1 filter)
# Use pan-starrs for photometry (grizy filters)
# Use panstarrs for photometry (grizy filters)
for refObjLoader in (config.ccdProcessor.calibrate.astromRefObjLoader,
                     config.ccdProcessor.calibrate.photoRefObjLoader,):
    refObjLoader.retarget(LoadIndexedReferenceObjectsTask)
config.ccdProcessor.calibrate.connections.astromRefCat = "gaia"
config.ccdProcessor.calibrate.astromRefObjLoader.ref_dataset_name = \
    config.ccdProcessor.calibrate.connections.astromRefCat
config.ccdProcessor.calibrate.astromRefObjLoader.filterMap = {
    "u": "phot_g_mean_mag",
    "g": "phot_g_mean_mag",
    "r": "phot_g_mean_mag",
    "i": "phot_g_mean_mag",
    "z": "phot_g_mean_mag",
    "y": "phot_g_mean_mag",
    "VR": "phot_g_mean_mag"}
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

