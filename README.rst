unsplash-download
=================

This little Python script allows you to download the fine public domain images
from http://unsplash.com

This will not download images that already exist, thus making it possible to
run this from a cron job.

Requirements
------------

- beautifulsoup4
- lxml
- docopt

Installation
------------

You can use pip/PyPI, which will automatically resolve all dependencies:

::

    pip install unsplash-download


To install unsplash-download you can also clone the repo and install it via 
setup.py:

::

    git clone https://github.com/mkzero/unsplash-download
    python2 setup.py install

After that you should be able to use the ``unsplash-download`` command from 
your command line.
