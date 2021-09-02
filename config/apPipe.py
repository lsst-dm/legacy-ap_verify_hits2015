# Config override for lsst.ap.pipe.ApPipeTask
import os.path
from lsst.utils import getPackageDir

configDir = os.path.dirname(__file__)
decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')

config.ccdProcessor.load(os.path.join(decamConfigDir, "processCcd.py"))

# Use CP calibrations
config.ccdProcessor.isr.load(os.path.join(configDir, 'isr.py'))

# Use dataset's reference catalogs
config.ccdProcessor.calibrate.load(os.path.join(configDir, 'calibrate.py'))

# Use dataset's specific templates
config.differencer.load(os.path.join(configDir, 'imageDifference.py'))
config.transformDiaSrcCat.load(os.path.join(configDir, 'transformDiaSrcCat.py'))
config.diaPipe.load(os.path.join(configDir, 'diaPipe.py'))
