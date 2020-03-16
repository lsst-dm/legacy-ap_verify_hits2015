# Config override for lsst.ap.pipe.ApPipeTask
import os.path
from lsst.utils import getPackageDir

configDir = os.path.dirname(__file__)
decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')

config.ccdProcessor.load(os.path.join(decamConfigDir, "processCcd.py"))

# Use dataset's reference catalogs
config.ccdProcessor.calibrate.load(os.path.join(configDir, 'calibrate.py'))

# Templates are deepCoadds assembled with the CompareWarp algorithm
config.differencer.coaddName = "deep"
config.differencer.getTemplate.coaddName = config.differencer.coaddName
config.differencer.getTemplate.warpType = "direct"
