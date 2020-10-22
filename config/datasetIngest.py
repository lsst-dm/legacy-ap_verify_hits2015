# Ignore wtmaps and illumcors
# These data products may be useful in the future, but are not yet supported by the Stack
# and will confuse the ingester
config.calibBadFiles = ['*_fcw_*', '*_zcw_*', '*_ici_*']

config.refcats = {
    'gaia': 'gaia_HiTS_2015.tar.gz',
    'panstarrs': 'ps1_HiTS_2015.tar.gz'
    }

# This option allows "community pipeline produced" calibrations to be
# ingested correctly, preventing the case in which some dates are
# unable to find the correct calibration.
config.calibIngester.register.incrementValidEnd = False
