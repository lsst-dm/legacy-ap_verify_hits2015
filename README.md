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
`repo`                | Butler repo into which raw data can be ingested. This should be copied to an appropriate location before ingestion. Currently contains the appropriate DECam `_mapper` file.
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

