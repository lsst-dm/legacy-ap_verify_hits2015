`verify_ap_dataset_template`
============================

Template repo for developing datasets for use with verify_ap.

This repo is designed to be used as a template for developing new data sets for integration into `verify_ap`.

It is currently set up for using `obs_test`.

Relevant Files and Directories
-----
path                  | description
:---------------------|:-----------------------------
`raw`                 | To be populated with photometrically and astrometrically calibrated data. Currently contains a single small fits file (taken from `obs_test`) to test `git-lfs` functionality.
`data`                | Butler repo of ingested raw data and processCcd results. Currently only contains `_mapper` file which should be modified.
`ref_cats`            | To be populated with relevant reference catalogs. Currently empty
`dataIds.list`        | List of dataIds in this repo. For use in running Tasks. Currently set to run all Ids.


Git LFS
-------

To clone and use this repository, you'll need Git Large File Storage (LFS).

Our [Developer Guide](http://developer.lsst.io/en/latest/tools/git_lfs.html) explains how to setup Git LFS for LSST development.

