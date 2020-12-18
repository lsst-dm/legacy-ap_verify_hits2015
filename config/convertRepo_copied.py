# Config overrides for convert_gen2_repo_to_gen3.py

config.datasetIncludePatterns = ["ref_cat"]

config.refCats = ['gaia', 'panstarrs']
for refcat in config.refCats:
    config.runs[refcat] = "refcats"

# Already stored in convertRepo_templates.py
config.doRegisterInstrument = False
