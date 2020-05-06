# Config overrides for convert_gen2_repo_to_gen3.py

# Pass only templates and their supporting types
config.datasetIncludePatterns = ["*Coadd*"]
config.datasetIgnorePatterns = []
for coaddType in ["deep", "goodSeeing", "dcr"]:
    config.runs[f"{coaddType}Coadd"] = f"templates/{coaddType}"
