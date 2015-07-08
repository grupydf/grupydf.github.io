#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import OrderedDict

AUTHOR = u'Grupy-DF'
SITENAME = u'Grupy-DF'
SITEURL = ''

TIMEZONE = 'America/Sao_Paulo'
THEME = "./.themes/materialize"

DEFAULT_LANG = u'pt'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORY_URL = 'blog/category/{slug}'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'

TAG_URL = 'blog/tag/{slug}'
TAG_SAVE_AS = 'blog/tag/{slug}.html'

INDEX_SAVE_AS = "blog/index.html"

#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Navbar Links
NAVBAR_LINKS = (
    {
        "title" : "Blog",
        "href": "blog",
    },
    {
        "title" : "Membros",
        "href": "membros",
    },
)

SOCIAL_LINKS = (
    {
        "href": "https://twitter.com/grupydf",
        "icon": "fa-twitter",
        "text": "Twitter",
    },
    {
        "href": "https://github.com/grupydf",
        "icon": "fa-github",
        "text": "GitHub",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/grupy-df",
        "icon": "fa-envelope",
        "text": "Mailing List",
    },
)

MEMBROS = OrderedDict((
    ("Biguá", {
        "email": "bigua.kun@gmail.com",
        "twitter": "@pixeledbird",
        "github": "bigua"
        }),
    ("Eduardo Henrique", {
        "email": "eduardohitek@gmail.com",
        "twitter": "@eduardohitek",
        "github": "eduardohitek"
        }),
    ("Gabriel Miranda", {
        "email": "gabrielm.car@gmail.com",
        "twitter": "@gblmiranda",
        "github": "gblmiranda"
        }),
    ("Humberto Rocha", {
        "email": "humrochagf@gmail.com",
        "twitter": "@humrochagf",
        "github": "humrochagf"
        }),
    ("Marco Rougeth", {
        "email": "marco@rougeth.com",
        "twitter": "@marcorougeth",
        "github": "rougeth"
        }),
    ("Pedro Henrique", {
        "email": "pedrohenriqueacruz@gmail.com",
        "twitter": "@phinfonet",
        "github": "phinfonet"
        }),
    ("Gilson Filho", {
        "email": "contatogilsonsbf@gmail.com",
        "twitter": "@gilsonfilho",
        "github": "gilsondev"
        }),
    ("Dirley Rodrigues", {
        "twitter": "@dirleyrls",
        "github": "ravishi"
        }),
    ("Wagner Santos", {
        "email": "wagnerjs.unb@gmail.com",
        "twitter": "@wagnerjsantos",
        "github": "wagnerjs"
        }),
    ("Israel P. Siqueira", {
        "email": "israelps@gmail.com",
        "twitter": "@israelps",
        "github": "israelps"
        }),
    ("Magnun Leno", {
        "email": "magnun.leno@gmail.com",
        "twitter": "@mind_bend",
        "github": "magnunleno",
        "site": {
            "nome": "Mind Bending",
            "href": "http://mindbending.org",
            }
        })
))
