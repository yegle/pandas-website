****************************
Python Data Analysis Library
****************************

*pandas* is an open source, BSD-licensed library providing powerful
lightweight data structures (and the capabilities to work with them) to the
`Python <http://www.python.org/>`__ programming language.

What are some of the main features of *pandas*?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are just a few of the things that *pandas* does well:

* Automatic and explicit **data alignment**: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let Series and DataFrame automatically align the data for you in computations
	
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

What problem does *pandas* solve?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python's strength is in the ability to naturally express high-level
abstraction using the language's human-readable syntax and object orientation.
To this, *pandas* adds the power to work with data usually found only in
domain-specific statistical programming languages.

When combined with the excellent `IPython <http://ipython.org/>`__ toolkit and
other libraries, the environment for doing data analysis in Python excels in
performance, productivity, and the ability to collaborate.

But lest we be accused of overselling you: we still lack the rich set of model
libraries other environments possess. You can help by porting them to Python!

*pandas* is a part of the `PyData project <http://www.github.com/pydata>`__,
an attempt to synthesize the best ideas from open source into one killer data
environment by combining the forces of the scientific community.

Why not just use R?
~~~~~~~~~~~~~~~~~~~

First of all, we love open source R! It set a new bar for powerful data
analysis, and provided much inspiration for *pandas*. R users will be pleased
to find this library adopts some of the best concepts of R, like the
foundational DataFrame. But *pandas* also seeks to solve some frustrations
common to R users.

* In R, manipulating data to clean up or align data sets is not automatic.
  Most real-world data sets are messy, so this distracts from analysis.

* Stretching the domain-specific R syntax to build systems relying on your
  models requires implementing non-computational logic is an unnatural and
  difficult way.

* In production systems at scale, R's performance is a bottleneck.

* Duck-taping R to a low-productivity systems language cripples the agility
  and maintainability of your systems.

And what about commercial alternatives? Many of them lack many of the basic
features of a modern open source programming language! In some cases, these
are the basics like abstraction and namespaces that allow you to build
libraries over time and work within a team,

The commercial alternatives have their place, but power users will eventually
find them limiting.

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

What about Java or C++?
~~~~~~~~~~~~~~~~~~~~~~~

While systems languages satisfy your need for performance, low-productivity
and low-maintainability are deal-breakers for a research environment. Some of
our users have found themselves able to replace Java systems with 20% as much
Python code!

Python + *pandas* is fast enough for most production use cases while still
providing all the advantages of an agile research environment.

Who do our users have to say?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	"*pandas* allows us to focus more on research and less on programming. We have found pandas easy to learn, easy to use, and easy to maintain. The bottom line is that it has increased our productivity."

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
