"""
cssbuster
--------------

cssbuster is a simple command line tool to invalidate
(when it's necessary) external resources linked to a css file.

"""


try:
    from setuptools import setup
    kw = {'entry_points':
          """[console_scripts]\ncssbuster = cssbuster:main\n""",
          'zip_safe': False}
except ImportError:
    from distutils.core import setup
    kw = {'scripts': ['cssbuster.py']}

setup(
    name='cssbuster',
    version='0.1.1',
    url='https://github.com/jorgebastida/cssbuster',
    license='BSD',
    author='Jorge Bastida',
    author_email='me@jorgebastida.com',
    description=("cssbuster is a simple command line tool to invalidate"
                 "(when it's necessary) external resources linked to a "
                 "css file."),
    long_description=__doc__,
    py_modules=['cssbuster'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'cssutils>=0.9.8'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    **kw
)
