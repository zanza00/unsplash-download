#!/usr/bin/env python
"""
unsplash-download - Downloads images from unsplash.com

Usage:
  unsplash-download <folder>
  unsplash-download <-n=photos_to_download>
  unsplash-download
  unsplash-download -h | --help
  unsplash-download -v | --version

Options:
  -h --help                 Show this screen
  -v --version              Show version
  -n <photos_to_download>   The Photos to Download

"""
import os
import re
import sys
import urllib.request
from docopt import docopt
from bs4 import BeautifulSoup
from itertools import count

DEBUG = False
ud_version = '1.0.2'

# arguments = docopt(__doc__, help=True, version='unsplash-download ' + ud_version)
# download_path = arguments['<folder>']
download_path = 'download'
base_url = 'https://unsplash.com'
img_per_page = 20
photos_to_download = 50  # TODO implement arbitrary number
link_search = re.compile("/photos/[a-zA-Z0-9-_]+/download")

if not os.path.exists(download_path):
    os.makedirs(download_path)

actual_img_number = 0
for page in count(start=1):
    url = "%s/?page=%s" % (base_url, page)
    print("Parsing page #%s %s" % (page, url))
    try:
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
        for current_img_number_in_page, tag in enumerate(soup.find_all(href=link_search), start=1):
            actual_img_number = (page - 1) * img_per_page + current_img_number_in_page
            if actual_img_number <= photos_to_download:
                print('Evaluating image #%s' % actual_img_number)
                image_id = str(tag['href']).split('/')[2]
                download_url = base_url + str(tag['href'])
                if os.path.exists("%s/%s.jpeg" % (download_path, image_id)):
                    print("Not downloading duplicate %s" % download_url)
                else:
                    print("Downloading %s" % download_url)
                    urllib.request.urlretrieve(
                            base_url + str(tag["href"]),
                            "%s/%s.jpeg" % (download_path, image_id)
                    )
            else:
                print('Downloaded all of %s images' % photos_to_download)
                break

    except urllib.error.HTTPError as e:
        print("HTML error. This would be all.")
        if DEBUG:
            print(e, file=sys.stderr)
        break
    except:
        print("An unknown error occurred", file=sys.stderr)
    else:
        if actual_img_number >= photos_to_download:
            print('script finished')
            break
