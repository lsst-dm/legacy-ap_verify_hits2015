# ap_verify_hits2015

Data from HiTS (2015) to verify the performance of alert production in the LSST Science Pipelines.

This and other `ap_verify` "datasets" are based on [ap_verify_dataset_template](https://github.com/lsst-dm/ap_verify_dataset_template).

Contains DECam data from the HiTS (2015) fields `Blind15A_26`, `Blind15A_40`, and `Blind15A_42`.

---
**Note**

This repository contains over 80 DECam images with 60+ CCDs each! If you want a smaller dataset to practice running `ap_verify`, consider `ap_verify_ci_hits2015` or `ap_verify_ci_cosmos_pdr2`.

At present, this repository can only be used for Gen 2 processing.
Support for the new Gen 3 pipeline framework is expected in the future.

---

Relevant Files and Directories
-----
path                  | description
:---------------------|:-----------------------------
`raw`                 | Raw, compressed DECam fits images from the HiTS (2015) fields `Blind15A_26`, `Blind15A_40`, and `Blind15A_42`.
`calib`               | DECam Community Pipeline MasterCalibs and `wtmap`s from the 2015 HiTS campaign. No raw images. See below for filename information.
`config`              | Dataset-specific configs to help the Science Pipelines work with this dataset.
`templates`           | Gen2 Butler repo containing good seeing g-band coadds and a skymap. For use as difference imaging templates.
`repo`                | A template for a Gen2 Butler raw data repository. This directory must never be written to; instead, it should be copied to a separate location, and data ingested into the copy (this is handled automatically by `ap_verify`, see below). Currently contains the appropriate DECam `_mapper` file.
`refcats`             | Tarballs of Gaia and PS1 reference catalogs in HTM format for regions overlapping all three HiTS fields.
`dataIds.list`        | List of dataIds for use in running Tasks. Currently set to run all Ids.
`preloaded`           | Starter Gen3 Butler repo containing a skymap as well as the refcats, calibs, and templates described above.

Master calibration file names
-----------------------------

Below are the different types of master calibration files in the `calib` directory:

* fci: dome flat images
* fcw: dome flat weight maps (not used)
* zci: zero/bias images
* zcw: zero/bias weight maps (not used)
* ici: illumcor images (not used)

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
