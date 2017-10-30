v0.21.0 Final (October 27, 2017)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a major release from 0.20.3 and includes a number of API changes, deprecations, new features,
enhancements, and performance improvements along with a large number of bug fixes. We recommend that all
users upgrade to this version.

Highlights include:

- Integration with `Apache Parquet <https://parquet.apache.org/>`__, including a new top-level ``read_parquet`` function and ``DataFrame.to_parquet`` method, see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-enhancements-parquet>`__.
- New user-facing dtype ``pandas.api.types.CategoricalDtype`` for specifying
  categoricals independent of the data, see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-enhancements-categorical-dtype>`__.
- The behavior of ``sum`` and ``prod`` on all-NaN Series/DataFrames is now consistent and no longer depends on whether `bottleneck <https://kwgoodman.github.io/bottleneck-doc/>`__ is installed, see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-api-breaking-bottleneck>`__.
- Compatibility fixes for pypy, see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-pypy>`__.
- Additions to the ``drop``, ``reindex`` and ``rename`` API to make them more consistent, see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-enhancements-drop-api>`__.
- Addition of the new methods ``DataFrame.infer_objects`` (see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-enhancements-infer-objects>`__) and ``GroupBy.pipe`` (see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-enhancements-groupby-pipe>`__).
- Indexing with a list of labels, where one or more of the labels is missing, is deprecated and will raise a KeyError in a future version, see `here <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-api-breaking-loc>`__.

Check the `API Changes <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-api-breaking>`__ and `deprecations <https://pandas.pydata.org/pandas-docs/version/0.21/whatsnew.html#whatsnew-0210-deprecations>`__ before updating.
