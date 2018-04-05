# Ignore wtmaps and illumcors
# These data products may be useful in the future, but are not yet supported by the Stack
# and will confuse the ingester
config.calibBadFiles = ['*_fcw_*', '*_zcw_*', '*_ici_*']

config.defectTarball = 'defects_2014-12-05.tar.gz'

config.refcats = {
    'gaia': 'gaia_HiTS_2015.tar.gz',
    'pan-starrs': 'ps1_HiTS_2015.tar.gz'
    }
