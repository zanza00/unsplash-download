#!/usr/bin/env python
"""
unsplash-download - Downloads images from unsplash.com

Usage:
  unsplash-download <folder>
  unsplash-download -h | --help
  unsplash-download -v | --version

Options:
  -h --help                 Show this screen
  -v --version              Show version

"""
import os
import re
import sys
import urllib.request
from docopt import docopt
from bs4 import BeautifulSoup, SoupStrainer

DEBUG = False
ud_version = '1.0.2'

# arguments = docopt(__doc__, help=True, version='unsplash-download ' + ud_version)
# download_path = arguments['<folder>']
download_path = 'download'
base_url = 'https://unsplash.com'
# page = 1
link_search = re.compile("/photos/[a-zA-Z0-9-]+/download")

if not os.path.exists(download_path):
    os.makedirs(download_path)

for page in range(1, 2):
    url = base_url + "/?page=" + str(page)
    print("Parsing page %s" % url)
    try:
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
        for tag in soup.find_all(href=link_search):
            image_id = str(tag['href']).split('/')[2]
            download_url = base_url + str(tag['href'])

            if os.path.exists("%s/%s.jpeg" % (download_path, image_id)):
                print("Not downloading duplicate %s" % download_url)
                continue

            print("Downloading %s" % download_url)
            urllib.request.urlretrieve(
                    base_url + str(tag["href"]),
                    "%s/%s.jpeg" % (download_path, image_id)
            )

    except urllib.error.HTTPError as e:
        print("HTML error. This would be all.")
        if DEBUG:
            print(e, file=sys.stderr)
        break
    # except HTMLParser.HTMLParseError as e:
    #     print('Error parsing the HTML', file=sys.stderr)
    #     if DEBUG:
    #         print(e, file=sys.stderr)
    except:
        print("An unknown error occured", file=sys.stderr)
