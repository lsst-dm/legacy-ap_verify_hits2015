# Config overrides for convert_gen2_repo_to_gen3.py

config.refCats = ['gaia', 'panstarrs']

# Need to specify runs for each refcat
for refcat in config.refCats:
    config.runs[refcat] = "refcats"
