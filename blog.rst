Pandas 0.20
===========

This has grown to be quite a release, so we thought it'd be worthwhile to write a bit more about what went into this release.
As always, the full `release notes`_ are available for a detailed description of all the changes.

New Highlights
==============

The release notes have a highlights section, so I'll just talk breifly about a couple of the new major ones: ``.agg`` and ``.transform``.
These methods should feel familiar to users; just like the Groupby versions.

New Module Privacy
==================

Like any project of reasonable size, pandas has developed a smattering of supporting modules to deliever that great experience you know and love.
Quite a few of these "internal" modules have been moved to new homes, as part of a broad effort make the code base more sensible and maintainable.

The fact that "internal" is in scare-quotes reveals a problem we had before.
Modules like ``pandas.lib.pyx`` were public, according to Python's conventions of designating private modules with a single leading underscore.
However, nothing in there was ever intended to be used by anyone outside pandas; methods in there were never included in our documentation. 

To clarify the situation, this release moved around a lot of code. See the `new module privacy`_ section for more.
This shouldn't affect most end users. Some library authors will need to release updates to avoid the deprecations.
Libraries like dask, statsmodels, and seaborn are already OK.

New Deprecations
================

We had two new deprecations of note in this cycle: ``Panel`` and ``.ix``.
It's a bit sad to see ``Panel`` go (it's at least partially responsible for pandas' moniker), but this has been a long-time coming.
Panel support has always been a bit behind the tabular-dataset workflows pandas has focused in on.
Fortunately there are other great projects like `xarray`_, and easy conversion with ``DataFrame.to_xarray`` for conversion.

The other big one is ``.ix``. This was tough because there's so much code out there using ``.ix``.

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
