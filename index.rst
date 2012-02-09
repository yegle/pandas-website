****************************
Python Data Analysis Library
****************************

*pandas* is an open source, BSD-licensed library providing high-performance,
easy-to-use data structures and data analysis tools for the `Python
<http://www.python.org/>`__ programming language.

What are some of the main features of *pandas*?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are just a few of the things that *pandas* does well:

* Intelligent **data alignment**: automatic label-based alignment in
  computations, and easily manipulate messy data into an orderly form

* Integrated **missing data** handling

* Size mutability: columns can be **inserted and deleted** from DataFrame and
  higher dimensional objects

* Powerful **group by** engine: perform split-apply-combine operations on data
  sets, for both aggregating and transforming data

* Intelligent label-based **slicing**, **fancy indexing**, and **subsetting**
  of large data sets;

* High performance **merging and joining** data sets;

* Flexible **reshaping** and pivoting of data sets

* **Hierarchical labeling** of axes: stack and unstack, possible to use
    multiple labels per tick

* Tools for reading and writing data to many different formats: CSV and text
  files, Microsoft Excel, databases, and the fast HDF5 format

* **Time series**-functionality: date range generation and frequency
  conversion, moving window statistics, moving window linear regressions, date
  shifting and lagging, create domain-specific time offsets, join time series
  without losing data.

What problem does *pandas* solve?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python has long been a tool of choice for data munging and preparation, but it
has been less well-suited for data analysis and modeling. *pandas* fills this
gap, enabling you to carry out your entire data analysis workflow in Python
without having to switch to a more domain specific language like R.

When combined with the excellent `IPython <http://ipython.org/>`__ toolkit and
other libraries, the environment for doing data analysis in Python excels in
performance, productivity, and the ability to collaborate.

*pandas* does not implement significant statistical modeling outside of linear
and panel regression; for this, look to the `statsmodels project
<http://statsmodels.sf.net>`__. More work is still needed to make Python a
first class statistical modeling environment, but we are well on our way toward
that goal.

.. *pandas* is a part of the `PyData project <http://www.github.com/pydata>`__,
.. an attempt to synthesize the best ideas from open source into one killer data
.. environment by combining the forces of the scientific community.

Why not R?
~~~~~~~~~~

First of all, we love open source R! It set a new bar for powerful data
analysis, and provided some inspiration for *pandas* features. R users will be
pleased to find this library adopts some of the best concepts of R, like the
foundational DataFrame. But *pandas* also seeks to solve some frustrations
common to R users.

* R's data alignment and indexing functionality are very barebones, leaving
  much work to the user. *pandas* makes working with messy, irregularly indexed
  data, such as time series data, easy and intuitive. *pandas* also provides
  rich tools like hierarchical indexing which are not to be found in R.

* R is not well-suited for general purpose programming and system
  development. *pandas* enables you to do robust, large-scale data processing
  seamlessly in your production application development.

* R's "copy-left" GPL license prevents its use in most commercial software
  development, compared with Python and pandas's permissive BSD license.

* Building a hybrid system with R connected to a low-productivity systems
  language like C++ or Java can cripple the agility and maintainability of your
  systems.

.. And what about commercial alternatives? Many of them lack many of the basic
.. features of a modern open source programming language! In some cases, these
.. are the basics like abstraction and namespaces that allow you to build
.. libraries over time and work within a team,

.. The commercial alternatives have their place, but power users will
.. eventually find them limiting.

Why use Python?
~~~~~~~~~~~~~~~

* The lightweight and user-friendly object orientation of Python makes it
  natural to express ideas in Python syntax. This ability to encapsulate
  results and analyze them in a high-level way is a great strength.

* Python is a high-productivity language. Novices find it accessible and
  experts are able to dramatically increase their output with concise code.

* Python is great for collaboration. The human-readable syntax improves
  working with other people's code.

* Python is maintainable. The clear and concise syntax makes working with
  legacy code tolerable.

* Python has a huge collection of well-tested and widely-deployed open
  source libraries to be leveraged in your project. It is relied upon by many
  of the largest technology companies.

Why add *pandas*?
~~~~~~~~~~~~~~~~~

* *pandas* adds the power and ease-of-use of well-designed in-memory data
  structures (and the capabilities to work with them) to the existing
  strengths of the Python language.

* *pandas* intelligently handles missing data and misaligned data sets,
  bringing unstructured or irregular data into a structured form. Less time is
  spent doing data manipulation, allowing you to focus on data analysis.

* When compared to data analysis tasks done in other interpreted languages,
  *pandas* has great advantages in performance. The library has been
  ruthlessly optimized, and critical code paths are compiled to C.

* These performance advantages, paired with the other strengths of Python,
  make it suitable for building production systems without changing
  development environments.

* Python with *pandas* is used in a wide variety of academic and commercial
  domains, including Finance, Neuroscience, Economics, Statistics,
  Advertising, Web Analytics, and more.

* Python and *pandas* are both open source, making them freely usable,
  modifiable, and distributable, even for commercial use.

What about Java, C++, and C#?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While systems languages satisfy your need for performance, low-productivity and
low-maintainability are deal-breakers for a research environment. Some of our
users have found themselves able to replace Java systems with 20% as much
Python code!

Python + *pandas* is fast enough for most production use cases while still
providing all the advantages of an agile research environment.

Who do our users have to say?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	"*pandas* allows us to focus more on research and less on programming. We
	have found pandas easy to learn, easy to use, and easy to maintain. The
	bottom line is that it has increased our productivity."

	.. image:: /_static/aqr_capital_management_logo.png
		:alt: AQR Capital Management Logo
		:align: right

| **Roni Israelov, PhD**
| Portfolio Manager
| `AQR Capital Management <http://www.aqr.com/>`_

.. toctree::
	:hidden:

	getpandas
	community
	developers
	talks
	commercialsupport
