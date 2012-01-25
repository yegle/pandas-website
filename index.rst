****************************
Python Data Analysis Library
****************************

*pandas* is an open source, BSD-licensed `Python <http://www.python.org/>`_
package providing fast, flexible, and expressive data structures designed to
make working with “relational” or “labeled” data both easy and intuitive.

What problem does *pandas* solve?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *pandas* library brings the capabilities found in common statistical
programming languages to Python, and then some. With the addition of *pandas*
and other important data libraries, Python has become the best way to do
powerful, real-world, in-memory data analysis.

Why Python + *pandas*?
~~~~~~~~~~~~~~~~~~~~~~

	* *pandas* provides all the power and agility of a statistical language with the general purpose utility of the Python language.
	* Python is a famously high-productivity language. Novices find it accessible and experts are able to dramatically increase their output of useful software. It is used by many of the top technology companies in the world.
	* Python is team-friendly. Because Python has all the trappings of a modern object oriented programming language and syntax that is human-readable, collaboration between multiple programmers (and even end users) is easy.
	* Python is easily maintainable. The same things that make Python excellent for collaboration also help projects avoid the deterioration over time found in most legacy systems.
	* Python has a huge collection of well-tested and widely-deployed open source libraries to be leveraged in your project.
	* *pandas* intelligently handles missing data and misaligned data sets, bringing unstructured or irregular data into a structured form, so you can focus on analyzing your data rather than manipulating it. In an ideal world, your data would be clean. Unfortunately, real data can be messy. 
	* Real-world systems demand speed. Python is a high-performance language, so *pandas* has also been diligently optimized for performance. The library is `benchmarked with vbench <http://pandas.sourceforge.net/vbench.html>`_, with critical code compiled to C. 
	* Python with *pandas* is used in a wide variety of academic and commercial domains, including Finance, Neuroscience, Economics, Statistics, Advertising, Web Analytics, and more.
	* Python and *pandas* are both open source, making them freely usable, modifiable, and distributable, even for commercial use.

Why not R (or one of its commercial alternative)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users will be pleased to find many of the best concepts from R readily
available in *pandas*, such as the foundational DataFrame. However, *pandas*
improves on R and commercial alternatives in several significant ways. With
other tools, you still run into problems with:

	* Spending too much effort manipulating data to clean up or align your data sets;
	* Stretching idiosyncratic statistical programming languages to implement non-computational logic best done in a general purpose language;
	* Building production systems in slow research environments that don't scale; or,
	* Starting over from scratch when you move from your research environment to a production-ready technology;
	* Maintaining expensive legacy systems instead of continuing to innovate;
	* In some cases with the commercial alternatives, you'll even be missing the basic features of a modern programming language, like abstraction and namespaces, that allow you to build libraries over time and work within a team!

Most of us need to implement non-computational business logic alongside our
data analysis while collaborating in a team environment. Python + *pandas* is
the best way to get the expressiveness and ease-of-use necessary for data
analysis with the performance and general purpose functionality demanded in
the real world.

Why not build my production system in Java or C++?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the real world, you need to deploy systems quickly and have the agility to
respond to changes. Tools like Java and the variations of C may satisfy your
need for performance, but they don't let you build, change, and maintain
systems as effectively or efficiently as Python, particularly if you work on a
team where multiple languages are used for different purposes.

Since high-performance Python + *pandas* is fast enough for production while
still providing the agility and maintainability real systems require, it can
be the foundation for every part of your tool chain. Some of our users have
found themselves able to replace Java systems with 20% as much Python code (or
less)!

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
