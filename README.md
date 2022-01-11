# ap_verify_hits2015

Data from HiTS (2015) to verify the performance of alert production in the LSST Science Pipelines.

This and other `ap_verify` "datasets" are based on [ap_verify_dataset_template](https://github.com/lsst-dm/ap_verify_dataset_template).

Contains g-band DECam data from the HiTS (2015) fields `Blind15A_26`, `Blind15A_40`, and `Blind15A_42`.

---
**Note**

This repository contains over 80 DECam images with 60+ CCDs each! If you want a smaller dataset to practice running `ap_verify`, consider `ap_verify_ci_hits2015` or `ap_verify_ci_cosmos_pdr2`.

Due to problems with detectors 2 and 61, this repository cannot process these detectors.
Because of this, you must specify this data-query argument when running ap_verify on this data (see [DM-32265](https://jira.lsstcorp.org/browse/DM-32265)):

```
--data-query "detector not in (2, 61)"
```

---

Relevant Files and Directories
-----
path                  | description
:---------------------|:-----------------------------
`raw`                 | Raw, compressed DECam fits images from the HiTS (2015) fields `Blind15A_26`, `Blind15A_40`, and `Blind15A_42`.
`config`              | Dataset-specific configs to help the Science Pipelines work with this dataset.
`pipelines`           | Dataset-specific pipelines to run on this dataset.
`dataIds.list`        | List of dataIds for use in running Tasks. Currently set to run all Ids.
`preloaded`           | Starter Gen3 Butler repo containing a skymap, DECam Community Pipeline MasterCalibs from the 2015 HiTS campaign, deep g-band coadds for use as differencing templates, and Gaia and PS1 reference catalogs in HTM format for regions overlapping any visit in the dataset.
`scripts`             | Scripts and data for generating this dataset.

Git LFS
-------

To clone and use this repository, you'll need Git Large File Storage (LFS).

Our [Developer Guide](http://developer.lsst.io/en/latest/tools/git_lfs.html) explains how to setup Git LFS for LSST development.

Usage
-----

`ap_verify_hits2015` is designed to be run using [`ap_verify`](https://pipelines.lsst.io/modules/lsst.ap.verify/), which is distributed as part of the `lsst_distrib` package of the [LSST Science Pipelines](https://pipelines.lsst.io/).

This dataset is not included in `lsst_distrib` and is not available through `newinstall.sh`.
However, it can be installed explicitly with the [LSST Software Build Tool](https://developer.lsst.io/stack/lsstsw.html) or by cloning directly:

    git clone https://github.com/lsst/ap_verify_hits2015/
    setup -r ap_verify_hits2015

See the Science Pipelines documentation for more detailed instructions on [installing datasets](https://pipelines.lsst.io/modules/lsst.ap.verify/datasets-install.html) and [running `ap_verify`](https://pipelines.lsst.io/modules/lsst.ap.verify/running.html). The name of this dataset is `HiTS2015`.
