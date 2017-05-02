Pandas 0.20
===========

This has grown to be quite a release, so we thought it'd be worthwhile to write a bit more about what went into this release.
As always, the full `release notes`_ are available for a detailed description of all the changes.


``ix`` Deprecation
==================


A big deprecation in 0.20.0 is the ``.ix`` indexing method. This was though because there's so much code out there using ``.ix``.
To illustrate *why* we decided to deprecate it, consider the following two Series objects:


.. code-block:: python

    >>> s1 = pd.Series(range(4), index=range(3, 7))

    >>> s2 = pd.Series(range(4), index=list('abcd'))

    In [15]: s1
    Out[15]: 
    2    0
    3    1
    4    2
    5    3
    dtype: int64

    In [16]: s2
    Out[16]: 
    a    0
    b    1
    c    2
    d    3
    dtype: int64


One series with an integer index and one with an index with strings. When using ``.ix`` with the same values provided, the behaviour however depends on the type of the index:

.. code-block:: python

    >>> s1.ix[1:3]
    2    0
    3    1
    dtype: int64

    >>> s2.ix[1:3]
    b    1
    c    2
    dtype: int64

So different rows were selected with the same indexing operation. This is because in the ``s1`` case, *label-based* indexing was used (rows with labels 1, 2 and 3), while in the ``s2`` case *positional* indexing was used (rows at integer position 1 and 2, so second and third row).

The fact that ``.ix`` could do both label-based and positional indexing caused confusion, and therefore we decided to deprecate it. Instead of using ``.ix`` and let pandas decide on label-based vs positional, you can explicitly use ``.loc`` or ``.iloc`` for label-based and positional indexing, respectively.    


New Highlights
==============

The release notes have a highlights section, so I'll just talk breifly about a couple of the new major ones: ``.agg`` and ``.transform``.
These methods should feel familiar to users; just like the Groupby versions.

New Module Privacy
==================

Like any project of reasonable size, pandas has developed a smattering of supporting modules to deliver that great experience you know and love.
Quite a few of these "internal" modules have been moved to new homes, as part of a broad effort make the code base more sensible and maintainable.

The fact that "internal" is in scare-quotes reveals a problem we had before.
Modules like ``pandas.lib.pyx`` were public, according to Python's conventions of designating private modules with a single leading underscore.
However, nothing in there was ever intended to be used by anyone outside pandas; methods in there were never included in our documentation. 

To clarify the situation, this release moved around a lot of code. See the `new module privacy`_ section for more.
This shouldn't affect most end users. Some library authors will need to release updates to avoid the deprecations.
Libraries like dask, statsmodels, and seaborn are already OK.

Are there methods or functions that have been moved or deprecated that you find very useful, but haven't gotten a public location to access it from?
If you have such a case, please open an issue on github to ask about the public/private status! 

New Deprecations
================

We had two new deprecations of note in this cycle: ``Panel`` and ``.ix``.

It's a bit sad to see ``Panel`` go (it's at least partially responsible for pandas' moniker), but this has been a long-time coming.
Panel support has always been a bit behind the tabular-dataset workflows pandas has focused in on. 
The 3-D structure of a Panel is much less common for many types of data analysis, than the 1-D of the Series or the 2-D of the DataFrame. Going forward it makes sense for pandas to focus on these areas exclusively.

Oftentimes, one can simply use a MultiIndex DataFrame for easily working with higher dimensional data. 
If you need higher dimensional data objects, fortunately there are other great projects like `xarray`_ that is much better suited for such kind of data. To easily try this out and convert your pandas objects to xarray, you can use the ``to_xarray`` method.


Towards 1.0
===========

Development focus is shifting to pandas 1.0.

Towards 2.0
===========

Work on `pandas 2`_ is ongoing.


.. _pandas2: https://github.com/pandas-dev/pandas2
.. _release notes: http://pandas.pydata.org/pandas-docs/version/0.20.0/
.. _xarray: http://xarray.pydata.org/en/stable/
.. _new module privacy: http://pandas-docs.github.io/pandas-docs-travis/whatsnew.html#whatsnew-0200-privacy
