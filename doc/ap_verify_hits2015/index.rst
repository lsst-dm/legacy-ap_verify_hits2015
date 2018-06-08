.. _ap_verify_hits2015-package:

##################
ap_verify_hits2015
##################

The ``ap_verify_hits2015`` package represents a small subset of the DECam `HiTS`_ survey.
It is a good example dataset for difference imaging with DECam.

.. _HiTS: https://doi.org/10.3847/0004-637X/832/2/155

Project info
============

Repository
   https://github.com/lsst/ap_verify_hits2015

.. Datasets do not have their own (or a collective) Jira components; by convention we include them in ap_verify

Jira component
   `ap_verify <https://jira.lsstcorp.org/issues/?jql=project %3D DM %20AND%20 component %3D ap_verify %20AND%20 text ~ "hits2015">`_

Dataset Contents
================

This package provides complete data for three fields from the 2015 `HiTS`_ survey.
It contains:

* raw images from the ``Blind15A_26``, ``Blind15A_40``, and ``Blind15A_42`` survey fields, in g band.
* biases (``zci``), flats (``fci``), and corresponding weight maps (``zcw``, ``fcw``) in all DECam bands (ugriz, Y, VR). [Note: weights are not currently used by `ap_verify` or `ap_pipe`]
* illumination corrections (``ici``) in g, r, and i band. [Note: illumcors are not currently used by `ap_verify` or `ap_pipe`]
* defect masks (``bpm``) from December 5, 2014.
* reference catalogs for Gaia DR1 and Pan-STARRS1, covering the raw images' footprint.
* image differencing templates coadded from HiTS 2014 data, covering the raw images' footprint.

Intended Use
============

This dataset is designed for medium-scale difference imaging analysis, using "deep" coadd templates, by ``ap_verify``.
It can also be used for difference imaging with single-image templates, but the single-season coverage of the raw data means the resulting difference images may be low quality.

The HiTS survey has a high cadence compared to other DECam datasets, so this dataset is good for testing cadence-sensitive applications.
