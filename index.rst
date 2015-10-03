****************************
Python Data Analysis Library
****************************

*pandas* is an open source, BSD-licensed library providing high-performance,
easy-to-use data structures and data analysis tools for the `Python
<http://www.python.org/>`__ programming language.

0.17.0 release candidate 2 (October 3, 2015)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**RELEASE CANDIDATE 2**


- compat for ``Python 3.5``
- compat for ``matplotlib 1.5.0``
- ``.convert_objects`` is now restored to the original, and is deprecated

This is a major release from 0.16.2 and includes a small number of API changes, several new features, enhancements, and performance improvements along with a large number of bug fixes. We recommend that all users upgrade to this version.

Highlights include:

- Release the Global Interpreter Lock (GIL) on some cython operations, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-gil>`__
- Plotting methods are now available as attributes of the .plot accessor, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-plot>`__
- The sorting API has been revamped to remove some long-time inconsistencies, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-api-breaking-sorting>`__
- Support for a ``datetime64[ns]`` with timezones as a first-class dtype, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-tz>`__
- The default for ``to_datetime`` will now be to raise when presented with unparseable formats, previously this would return the original input, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-api-breaking-to-datetime>`__
- The default for ``dropna`` in ``HDFStore`` has changed to ``False``, to store by default all rows even if they are all NaN, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-api-breaking-hdf-dropna>`__
- Datetime accessor (``dt``) now supports ``Series.dt.strftime`` to generate formatted strings for datetime-likes, and ``Series.dt.total_seconds`` to generate each duration of the timedelta in seconds. See `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-strftime>`__
- Period and PeriodIndex can handle multiplied freq like 3D, which corresponding to 3 days span. See `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-periodfreq>`__
- Development installed versions of pandas will now have PEP440 compliant version strings `GH9518 <https://github.com/pydata/pandas/issues/9518>`__
- Development support for benchmarking with the Air Speed Velocity library `GH8316 <https://github.com/pydata/pandas/pull/8316>`__
- Support for reading SAS xport files, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-enhancements-sas-xport>`__
- Removal of the automatic TimeSeries broadcasting, deprecated since 0.8.0, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-prior-deprecations>`__
- Display format with plain text can optionally align with Unicode East Asian Width, see `here <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0170-east-asian-width>`__
- Compatibility with Python 3.5 `GH11097 <https://github.com/pydata/pandas/issues/11097>`__
- Compatibility with matplotlib 1.5.0 `GH11111 <https://github.com/pydata/pandas/issues/11111>`__


See the `Whatsnew <http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html>`__ for much more information. Please report any issues `here <https://github.com/pydata/pandas/issues/10848>`__

Best way to Install
~~~~~~~~~~~~~~~~~~~

Best way to get this release-candidate is to install via `conda <http://pandas-docs.github.io/pandas-docs-travis/install.html#installing-pandas-with-anaconda>`__ from our development channel. Builds for ``osx-64,linux-64,win-64`` for ``Python 2.7 and Python 3.4`` are all available.

``conda install pandas -c pandas``


Quick vignette
~~~~~~~~~~~~~~

.. raw:: html

    <iframe src="http://player.vimeo.com/video/59324550" width="500"
    height="309" frameborder="0" webkitAllowFullScreen mozallowfullscreen
    allowFullScreen></iframe> <p><a href="http://vimeo.com/59324550">10-minute
    tour of pandas</a> from <a href="http://vimeo.com/user10077863">Wes
    McKinney</a> on <a href="http://vimeo.com">Vimeo</a>.</p>

What problem does *pandas* solve?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python has long been great for data munging and preparation, but less so for
data analysis and modeling. *pandas* helps fill this gap, enabling you to
carry out your entire data analysis workflow in Python without having to
switch to a more domain specific language like R.

Combined with the excellent `IPython <http://ipython.org/>`__ toolkit and
other libraries, the environment for doing data analysis in Python excels in
performance, productivity, and the ability to collaborate.

*pandas* does not implement significant modeling functionality outside of
linear and panel regression; for this, look to `statsmodels
<http://statsmodels.sf.net>`__ and `scikit-learn
<http://scikit-learn.org>`__. More work is still needed to make Python a first
class statistical modeling environment, but we are well on our way toward that
goal.

What do our users have to say?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	.. image:: /_static/aqr_capital_management_logo.png
		:alt: AQR Capital Management Logo
		:align: right
		:target: http://www.aqr.com/

| **Roni Israelov, PhD**
| Portfolio Manager
| `AQR Capital Management <http://www.aqr.com/>`__

	"*pandas* allows us to focus more on research and less on programming. We
	have found *pandas* easy to learn, easy to use, and easy to maintain.
	The bottom line is that it has increased our productivity."

	.. image:: /_static/appnexus_logo.png
		:alt: AppNexus Logo
		:align: right
		:target: http://www.appnexus.com/

| **David Himrod**
| Director of Optimization & Analytics
| `AppNexus <http://www.appnexus.com/>`__

	"*pandas* is the perfect tool for bridging the gap between rapid
	iterations of ad-hoc analysis and production quality code. If you
	want one tool to be used across a multi-disciplined organization of
	engineers, mathematicians and analysts, look no further."

	.. image:: /_static/datadog_logo.png
		:alt: Datadog Logo
		:align: right
		:target: http://www.datadoghq.com/

| **Olivier Pomel**
| CEO
| `Datadog <http://www.datadoghq.com/>`__

	"We use *pandas* to process time series data on our production servers.
	The simplicity and elegance of its API, and its high level
	of performance for high-volume datasets, made it a perfect choice for
	us."

.. toctree::
	:hidden:

	getpandas
	community
	talks

Library Highlights
~~~~~~~~~~~~~~~~~~

* A fast and efficient **DataFrame** object for data manipulation with
  integrated indexing;

* Tools for **reading and writing data** between in-memory data structures and
  different formats: CSV and text files, Microsoft Excel, SQL databases, and
  the fast HDF5 format;

* Intelligent **data alignment** and integrated handling of **missing data**:
  gain automatic label-based alignment in computations and easily manipulate
  messy data into an orderly form;

* Flexible **reshaping** and pivoting of data sets;

* Intelligent label-based **slicing**, **fancy indexing**, and **subsetting**
  of large data sets;

* Columns can be inserted and deleted from data structures for **size
  mutability**;

* Aggregating or transforming data with a powerful **group by** engine
  allowing split-apply-combine operations on data sets;

* High performance **merging and joining** of data sets;

* **Hierarchical axis indexing** provides an intuitive way of working with
  high-dimensional data in a lower-dimensional data structure;

* **Time series**-functionality: date range generation and frequency
  conversion, moving window statistics, moving window linear regressions, date
  shifting and lagging. Even create domain-specific time offsets and join time
  series without losing data;

* Highly **optimized for performance**, with critical code paths written in
  `Cython <http://www.cython.org/>`__ or C.

* Python with *pandas* is in use in a wide variety of **academic and
  commercial** domains, including Finance, Neuroscience, Economics,
  Statistics, Advertising, Web Analytics, and more.
