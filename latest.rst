v0.21.0 RC1 (October 13, 2017)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a major release from 0.20.3 and includes a number of API
changes, deprecations, new features, enhancements, and performance
improvements along with a large number of bug fixes. We recommend that
all users upgrade to this version.

Highlights include:

* Integration with `Apache Parquet <https://parquet.apache.org/>`__,
  including a new top-level ``read_parquet`` function and
  ``DataFrame.to_parquet`` method, see `here <https://pandas.pydata.org/pandas-docs/stable/io.html#io-parquet>`__

* New user-facing pandas.api.types.CategoricalDtype for specifying
  categoricals independent of the data, see `here <https://pandas.pydata.org/pandas-docs/stable/whatsnew.html#whatsnew-0210-enhancements-categorical-dtype>`__

* The behavior of sum and prod on all-NaN Series/DataFrames is now
  consistent and no longer depends on whether bottleneck is installed,
  see `here <https://pandas.pydata.org/pandas-docs/stable/whatsnew.html#whatsnew-0210-api-breaking-bottleneck>`__

* Compatibility fixes for pypy, see `here <https://pandas.pydata.org/pandas-docs/stable/whatsnew.html#whatsnew-0210-pypy>`__

Check the API Changes `whatsnew <https://pandas.pydata.org/pandas-docs/stable/whatsnew.html#whatsnew-0210-api-breaking>`__ and `deprecations <https://pandas.pydata.org/pandas-docs/stable/whatsnew.html#whatsnew-0210-deprecations>`__ before updating.

