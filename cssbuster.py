#!/usr/bin/env python
import os
import sys
import hashlib
import logging
from functools import partial
from optparse import OptionParser

import cssutils


resource_extra_cache = {}


def cache_bust_replacer(options, css_path, img_rel_path, resource_url,
                        stderr=None, cache=None):
    stderr = stderr or sys.stderr
    cache = cache or resource_extra_cache
    if not resource_url.startswith(('http://', 'https://')):
        url = resource_url.split('/')
        found = False
        for i in xrange(len(url)):
            test_path = os.path.join(img_rel_path, '/'.join(url[i:]))
            if os.path.exists(test_path):
                found = True
                break
        if found:
            if test_path not in cache:
                if options.sha1:
                    resource_file = open(test_path)
                    extra = hashlib.sha1(resource_file.read()).hexdigest()[:8]
                    resource_file.close()
                else:
                    extra = int(os.stat(test_path).st_mtime)
                cache[test_path] = extra
            else:
                extra = cache.get(test_path)
            resource_url = "%s?%s" % (resource_url, extra)
        else:
            stderr.write("WARNING: Resource %s not found\n" % css_path)
    else:
        stderr.write("WARNING: Absolute url to %s\n" % resource_url)
    return resource_url


def main():
    parser = OptionParser(usage="usage: %prog [options] css img")

    parser.add_option("-m", "--minified", action="store_true", dest="minified",
                      help="Minifi the css.")

    parser.add_option("--sha1", action="store_true", dest="sha1",
                      help=("Use sha1 insted the mtime (Most recent content "
                            "modification)"))

    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.error("You must provide a css file ")
    elif len(args) == 1:
        parser.error(("You must provide the relative path between "
                      "the css and the images."))

    css_path = os.path.basename(args[0])
    img_rel_path = args[1]

    # Configure the logger
    log = logging.getLogger('csscache')
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.ERROR)
    log.addHandler(handler)

    if options.minified:
        cssutils.ser.prefs.useMinified()

    # Create the parser
    parser = cssutils.CSSParser(log=log,
                                raiseExceptions=False,
                                parseComments=not options.minified,
                                validate=False)

    # Parse the original file
    sheet = parser.parseFile(args[0])

    # Replace all the urls
    replacer = partial(cache_bust_replacer, options, css_path, img_rel_path)
    cssutils.replaceUrls(sheet, replacer, ignoreImportRules=True)

    # print the new css
    print sheet.cssText

if __name__ == "__main__":
    main()
