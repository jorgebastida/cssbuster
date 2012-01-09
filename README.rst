csscachebuster
==============

cssbuster is a simple command line tool to invalidate (when it's necessary) external resources linked to a css file.

Features
--------
* Invalidate external resources used on a css file.
* Optionally minify the output css.

Example
-------

``cssbuster`` only needs two arguments. The first one is the name of the CSS file
you want to process, and the second one the path where ``cssbuster`` can locate the resources.

For a file named ``styles.css``:

    $ cssbuster styles.css ../img > styles.min.css


If you also want to minify it:

    $ cssbuster styles.css ../img --minified > styles.min.css

Limitations
-----------
* Currently cssbuster will only bust the relative and absolute resources, not the full ones ``http://...``
* This is an Alpha release, be aware!
