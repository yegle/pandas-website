****************************
Python Data Analysis Library
****************************

*pandas* is an open source, BSD-licensed library providing high-performance,
easy-to-use data structures and data analysis tools for the `Python
<http://www.python.org/>`__ programming language.

0.10.0 beta 1 (December 11, 2012)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first beta of pandas version 0.10.0 has now been released. This major
release includes the new high performance file parser engine, lots of new
features, performance improvements, and bug fixes. There are also a number of
necessary API changes; if you're a heavy pandas user, definitely look carefully
at the `What's New page
<http://pandas.pydata.org/pandas-docs/dev/whatsnew.html>`_.

Find binaries and source archives for v0.10.0b1 `here
<http://pandas.pydata.org/pandas-build/dev/>`_

Note we are posting stable daily development builds of the pandas windows
binaries `here <http://pandas.pydata.org/pandas-build/dev/>`_. You can download
them via the `Development Version <getpandas.html#development-version>`_
section of the "get pandas" page.

What problem does *pandas* solve?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python has long been great for data munging and preparation, but less so for
data analysis and modeling. *pandas* helps fill this gap, enabling you to
carry out your entire data analysis workflow in Python without having to
switch to a more domain specific language like R.

Combined with the excellent `IPython <http://ipython.org/>`__ toolkit and
other libraries, the environment for doing data analysis in Python excels in
performance, productivity, and the ability to collaborate.

*pandas* does not implement significant statistical modeling outside of linear
and panel regression; for this, look to the `statsmodels project
<http://statsmodels.sf.net>`__. More work is still needed to make Python a
first class statistical modeling environment, but we are well on our way
toward that goal.

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

* The library has been ruthlessly **optimized for performance**, with critical
  code paths compiled to C;

* Python with *pandas* is in use in a wide variety of **academic and
  commercial** domains, including Finance, Neuroscience, Economics,
  Statistics, Advertising, Web Analytics, and more.

Why not R?
~~~~~~~~~~

First of all, we love open source R! It is the most widely-used open source
environment for statistical modeling and graphics, and it provided some early
inspiration for *pandas* features. R users will be pleased to find this
library adopts some of the best concepts of R, like the foundational
DataFrame (one user familiar with R has described *pandas* as "R data.frame on
steroids"). But *pandas* also seeks to solve some frustrations common to R
users:

* R has barebones data alignment and indexing functionality, leaving much work
  to the user. *pandas* makes it easy and intuitive to work with messy,
  irregularly indexed data, like time series data. *pandas* also provides rich
  tools, like hierarchical indexing, not found in R;

* R is not well-suited to general purpose programming and system
  development. *pandas* enables you to do large-scale data processing
  seamlessly when developing your production applications;

* Hybrid systems connecting R to a low-productivity systems language like
  Java, C++, or C# suffer from significantly reduced agility and
  maintainability, and you're still stuck developing the system components in
  a low-productivity language;

* The "copyleft" GPL license of R can create concerns for commercial software
  vendors who want to distribute R with their software under another license.
  Python and *pandas* use more permissive licenses.

What about Java, C++, and C#?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While systems languages satisfy your need for performance, low-productivity
and low-maintainability are deal-breakers for a research environment. Some of
our users have found themselves able to replace Java systems with 20% as much
Python code!

Python + *pandas* is fast enough for most production use cases while still
providing all the advantages of an agile research environment.

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
	commercialsupport
	developers
