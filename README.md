# ap_verify_hits2015

Data from HiTS (2015) to verify the performance of alert production in the LSST DM stack.

Contains DECam data from the HiTS (2015) fields `Blind15A_26`, `Blind15A_40`, and `Blind15A_42`.

Relevant Files and Directories
-----
path                  | description
:---------------------|:-----------------------------
`raw`                 | Raw, compressed DECam fits images from the HiTS (2015) fields `Blind15A_26`, `Blind15A_40`, and `Blind15A_42`.
`calib`               | DECam master calibs and `wtmap`s from the 2015 HiTS campaign. No raw images. See below for filename information.
`config`              | Dataset-specific configs to help Stack code work with this dataset.
`templates`           | Butler repo containing coadded images intended to be used as templates.
`repo`                | A template for a Butler raw data repository. This directory must never be written to; instead, it should be copied to a separate location, and data ingested into the copy (this is handled automatically by `ap_verify`, see below). Currently contains the appropriate DECam `_mapper` file.
`refcats`             | Tarballs of Gaia and PS1 reference catalogs in HTM format for regions overlapping all three HiTS fields.
`dataIds.list`        | List of dataIds for use in running Tasks. Currently set to run all Ids.

Master calibration file names
-----------------------------

Below are the different types of master calibration files in the `calib` directory:

* fci: dome flat images
* fcw: dome flat weight maps
* zci: zero/bias images
* zcw: zero/bias weight maps
* ici: illumcor images

Git LFS
-------

To clone and use this repository, you'll need Git Large File Storage (LFS).

Our [Developer Guide](http://developer.lsst.io/en/latest/tools/git_lfs.html) explains how to setup Git LFS for LSST development.

Usage
-----

<!-- TODO: replace with just links to Sphinx labels `ap-verify-datasets-install` and `ap-verify-running` once those docs are published -->

This dataset must be cloned (with Git LFS) and set up with [EUPS](https://developer.lsst.io/stack/eups-tutorial.html) before it can be processed with `ap_verify`:

    git clone https://github.com/lsst/ap_verify_hits2015/
    setup -r ap_verify_hits2015

Then, run `ap_verify` to ingest and process the dataset through the AP pipeline:

    ap_verify.py --dataset HiTS2015 --id "visit=411822 ccdnum=25 filter=g" --output /my_output_dir/ --silent

or, instead, run `ingest_dataset` to create standard Butler repositories for other purposes

    ingest_dataset.py --dataset HiTS2015 --output /my_output_dir/

See the [`ap_verify`](https://github.com/lsst-dm/ap_verify/) documentation for more details.
