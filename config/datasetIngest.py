# Ignore wtmaps and illumcors
# These data products may be useful in the future, but are not yet supported by the Stack
# and will confuse the ingester
config.calibBadFiles = ['*_fcw_*', '*_zcw_*', '*_ici_*']

config.refcats = {
    'gaia': 'gaia_HiTS_2015.tar.gz',
    'panstarrs': 'ps1_HiTS_2015.tar.gz'
    }
