#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(name='unsplash-download',
      version='1.0.0',
      description='unsplash.com image downloader',
      long_description=long_description,
      author='Maik Kulbe',
      author_email='info@linux-web-development.de',
      license='MIT',
      packages=['unsplash_download'],
      entry_points = {
        "console_scripts": [
          "unsplash-download = unsplash_download.unsplash_download:main",
        ],
      },
      install_requires=[
        'beautifulsoup4',
        'lxml',
	'docopt'
      ],
    )
