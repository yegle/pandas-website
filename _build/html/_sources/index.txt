****************************
Python Data Analysis Library
****************************

*pandas* is an open source, BSD-licensed `Python <http://www.python.org/>`_ package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.

What problem does *pandas* solve?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *pandas* library brings the capabilities found in common statistical programming languages - and then some - to Python, providing the fundamental building blocks for doing practical, real-world data analysis.

	* In an ideal world, your data would be clean. Unfortunately, real data can be messy. *pandas* intelligently handles missing data and misaligned data sets - bringing unstructured, irregular data into a structured form - so you can focus on analyzing your data rather than manipulating it.
	* While some people are lucky enough to be working on strictly computational problems, most of us need to implement non-computational business logic alongside our data analysis. *pandas* provides all the power and agility of a statistical tool with the general purpose utility of the Python language.
	* Production systems demand speed, so *pandas* is optimized for performance. The library is benchmarked with `vbench <https://github.com/wesm/vbench>`_, with critical code compiled to C.

Why not use R (or MATLAB, SAS, SQL, etc.)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R users will be pleased to find many of the best concepts from that language readily available in *pandas*, such as the foundational DataFrame. However, pandas strays from the well-paved road in a number of significant ways. With other tools, you would still have problems with:

	* Spending too much effort manipulating data to clean up or align your data sets;
	* Stretching idiosyncratic statistical programming languages to implement non-computational logic best done in a general purpose language;
	* Building production systems in slow research environments that don't scale; or,
	* Starting over from scratch when you move from your research environment to a production-ready technology;
	* In some cases, you'll even be missing the basic features of a modern programming language, like abstraction and namespaces, that allow you to build libraries and work within a team!

*pandas* is built to solve what we call "the research-production gap". It's the best way to get the expressiveness and ease-of-use necessary for research with the performance and general purpose functionality necessary for production systems.

Why not build my production system in C or Java?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your models will change before your production system is even ready to deploy! In the real world, you need the agility to respond to change quickly, but tools like Java and C - while satisfying your need for speed - don't let you react to change quickly enough (particularly if you work on a team where half your colleagues are working in a different language!). Python + *pandas* is agile enough for research and fast enough for production.

Who do our users have to say?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	.. image:: /_static/aqr_capital_management_logo.png
		:alt: AQR Capital Management Logo
		:align: right

	"*pandas* provides a useful set of tools that allow us to focus on research and less on programming, where we can conveniently test our ideas in an interpreted environment. Using *pandas*'s econometrics library we can perform much of our analysis 'natively' without having to wrap 3rd party components. The sparse data handling functionality allowed us to expand its use to high frequency / intraday data analysis. It performs well under various use cases because critical components have been optimized in lower level languages. We have found *pandas* easy to learn, easy to use, and easy to maintain and the bottom line is that it has increased our productivity."

| **Roni Israelov, PhD**
| Portfolio Manager
| `AQR Capital Management <http://www.aqr.com/>`_

What are some of the main features of *pandas*?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are just a few of the things that *pandas* does well:

	* Automatic and explicit **data alignment**: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let Series and DataFrame automatically align the data for you in computations;
	* Easy handling of **missing data** (represented as NaN) in floating point as well as non-floating point data;
	* Size mutability: columns can be **inserted and deleted** from DataFrame and higher dimensional objects;
	* Powerful, flexible **group by**: perform split-apply-combine operations on data sets, for both aggregating and transforming data;
	* Make it **easy to convert** ragged, differently-indexed data in other Python and NumPy data structures into DataFrame objects;
	* Intelligent label-based **slicing**, **fancy indexing**, and **subsetting** of large data sets;
	* Intuitive **merging and joining** data sets;
	* Flexible **reshaping** and pivoting of data sets: no more munging column names!;
	* **Hierarchical labeling** of axes: stack and unstack, possible to use multiple labels per tick;
	* Robust IO tools for loading data from **flat files** (CSV and delimited), Excel files, databases, and saving / loading data from the ultrafast **HDF5** format;
	* **Time series**-specific functionality: date range generation and frequency conversion, moving window statistics, moving window linear regressions, date shifting and lagging, create domain-specific time offsets, join time series without losing data.
	
.. toctree::
	:hidden:
	
	getpandas
	community
	commercialsupport
