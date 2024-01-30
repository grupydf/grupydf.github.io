#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://grupydf.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'blog/feeds.atom'
FEED_ALL_RSS = 'blog/feeds.rss'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "grupydf"
DISQUS_NO_ID = True

# Following items are often useful when publishing

#GOOGLE_ANALYTICS = ""
