csscachebuster
==============

csscachebuster is a simple command line tool to invalidate (when it's necessary) external resources linked to a css file.

Features
--------
* Invalidate external resources used on a css file.
* Optionally minify the output css.

Example
-------

For a file named ``styles.css``::

    $ csscachebuster styles.css > styles.min.css


If you also want to minify it::

    $ csscachebuster styles.css --minified > styles.min.css
