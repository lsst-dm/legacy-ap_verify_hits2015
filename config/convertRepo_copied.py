# Config overrides for convert_gen2_repo_to_gen3.py

config.datasetIncludePatterns = ["ref_cat", "defects"]

config.refCats = ['gaia', 'panstarrs']
for refcat in config.refCats:
    config.runs[refcat] = "refcats"

# Already stored in convertRepo_calibs.py
config.doRegisterInstrument = False
config.doWriteCuratedCalibrations = False
