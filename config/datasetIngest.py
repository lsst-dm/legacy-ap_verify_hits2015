import os.path

from lsst.utils import getPackageDir
from lsst.obs.decam.ingest import DecamIngestTask

obsConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')

config.dataIngester.retarget(DecamIngestTask)
config.dataIngester.load(os.path.join(obsConfigDir, 'ingest.py'))

config.calibIngester.load(os.path.join(obsConfigDir, 'ingestCalibs.py'))
# Ignore wtmaps and illumcors
# These data products may be useful in the future, but are not yet supported by the Stack
# and will confuse the ingester
config.calibBadFiles = ['*_fcw_*', '*_zcw_*', '*_ici_*']

config.defectIngester.load(os.path.join(obsConfigDir, 'ingestCalibs.py'))
config.defectTarball = 'defects_2014-12-05.tar.gz'

config.refcats = {
    'gaia': 'gaia_HiTS_2015.tar.gz',
    'pan-starrs': 'ps1_HiTS_2015.tar.gz'
    }
