****************************
Python Data Analysis Library
****************************


*pandas* is an open source, BSD-licensed library providing high-performance,
easy-to-use data structures and data analysis tools for the `Python
<http://www.python.org/>`__ programming language.

*pandas* is a `NUMFocus <http://www.numfocus.org/open-source-projects.html>`__ sponsored project. This will help ensure the success of development of *pandas* as a world-class open-source project, and makes it possible to :doc:`donate <donate>` to the project.

.. image:: /_static/SponsoredProjectStamp_300px.png
	:alt: NUMFocus Logo
	:target: http://www.numfocus.org/open-source-projects.html

.. include:: latest.rst

.. include:: previous.rst


Best way to Install
~~~~~~~~~~~~~~~~~~~

The best way to get pandas is via `conda <http://pandas.pydata.org/pandas-docs/stable/install.html#installing-pandas-with-anaconda>`__

``conda install pandas``

Packages are available for `all supported python versions <http://pandas.pydata.org/pandas-docs/stable/install.html#python-version-support>`__
on Windows, Linux, and MacOS.

Wheels are also uploaded to `PyPI <https://pypi.org/project/pandas/>`__ and can be installed with

.. code-block:: shell

   pip install pandas


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

	about
	getpandas
	community
	talks
	donate

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
