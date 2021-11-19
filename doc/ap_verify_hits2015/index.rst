.. _ap_verify_hits2015-package:

##################
ap_verify_hits2015
##################

The ``ap_verify_hits2015`` package represents a small subset of the DECam `HiTS`_ survey, formatted for use with :doc:`lsst.ap.verify </modules/lsst.ap.verify/index>`.
It is a good example dataset for difference imaging with DECam.

.. _HiTS: https://doi.org/10.3847/0004-637X/832/2/155

.. _ap_verify_hits2015-using:

Using ap_verify_hits2015
========================

This dataset is designed for medium-scale difference imaging analysis, using "deep" coadd templates, by :doc:`lsst.ap.verify </modules/lsst.ap.verify/index>`.
It can also be used for difference imaging with single-image templates, but the single-season coverage of the raw data means the resulting difference images may be low quality.

The HiTS survey has a high cadence compared to other DECam datasets, so this dataset is good for testing cadence-sensitive applications.

.. _ap_verify_hits2015-contents:

Dataset contents
================

This package provides complete g-band data for three fields from the 2015 `HiTS`_ survey.
It contains:

* 28 visits to ``Blind15A_26``: visit IDs 410915, 410971, 411021, 411055, 411255, 411305, 411355, 411406, 411456, 411657, 411707, 411758, 411808, 411858, 412060, 412250, 412307, 412504, 412554, 412604, 412654, 412704, 413635, 413680, 415314, 415364, 419791, 421590
* 28 visits to ``Blind15A_40``: visit IDs 410929, 410985, 411035, 411069, 411269, 411319, 411369, 411420, 411470, 411671, 411721, 411772, 411822, 411872, 412074, 412264, 412321, 412518, 412568, 412618, 412668, 412718, 413649, 413694, 415328, 415378, 419802, 421604
* 28 visits to ``Blind15A_42``: visit IDs 410931, 410987, 411037, 411071, 411271, 411321, 411371, 411422, 411472, 411673, 411724, 411774, 411824, 411874, 412076, 412266, 412324, 412520, 412570, 412620, 412670, 412720, 413651, 413696, 415330, 415380, 419804, 421606
* biases (``zci``) and flats (``fci``).
* bias and flat weight maps (``zcw``, ``fcw``). [Note: weights are not currently used by ``ap_verify`` or ``ap_pipe``]
* illumination corrections (``ici``). [Note: illumcors are not currently used by ``ap_verify`` or ``ap_pipe``]
* reference catalogs for Gaia and Pan-STARRS1, covering the raw images' footprint.
* image differencing templates coadded from HiTS 2014 data, covering the raw images' footprint.

.. _ap_verify_hits2015-contributing:

Contributing
============

``ap_verify_hits2015`` is developed at https://github.com/lsst/ap_verify_hits2015.
You can find Jira issues for this module under the `ap_verify <https://jira.lsstcorp.org/issues/?jql=project%20%3D%20DM%20AND%20component%20%3D%20ap_verify%20AND%20text~"hits2015">`_ component.

.. If there are topics related to developing this module (rather than using it), link to this from a toctree placed here.

.. .. toctree::
..    :maxdepth: 1
