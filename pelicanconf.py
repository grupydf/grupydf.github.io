#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Grupy-DF'
SITENAME = u'Grupy-DF'
SITEURL = ''

TIMEZONE = 'America/Sao_Paulo'
THEME = "./.themes/materialize"

DEFAULT_LANG = u'pt'

ARTICLE_URL = 'artigos/{slug}'
ARTICLE_SAVE_AS = 'artigos/{slug}.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORY_URL = 'artigos/category/{slug}'
CATEGORY_SAVE_AS = 'artigos/category/{slug}.html'

TAG_URL = 'artigos/tag/{slug}'
TAG_SAVE_AS = 'artigos/tag/{slug}.html'

INDEX_SAVE_AS = "artigos/index.html"

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
        "title" : "Artigos",
        "href": "/artigos",
    },
    {
        "title" : "Equipe",
        "href": "/equipe",
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

EQUIPE = (
    { "nome": "Biguá",
        "email": "bigua.kun@gmail.com",
        "twitter": "@pixeledbird",
        "github": "bigua"
    },
    {
        "nome": "Eduardo Henrique",
        "email": "eduardohitek@gmail.com",
        "twitter": "@eduardohitek",
        "github": "eduardohitek"
    },
    {
        "nome": "Gabriel Miranda",
        "email": "gabrielm.car@gmail.com",
        "twitter": "@gblmiranda",
        "github": "gblmiranda"
    },
    {
        "nome": "Humberto Rocha",
        "email": "humrochagf@gmail.com",
        "twitter": "@humrochagf",
        "github": "humrochagf"
    },
    {
        "nome": "Marco Rougeth",
        "email": "marco@rougeth.com",
        "twitter": "@marcorougeth",
        "github": "rougeth"
    },
    {
        "nome": "Pedro Henrique",
        "email": "pedrohenriqueacruz@gmail.com",
        "twitter": "@phinfonet",
        "github": "phinfonet"
    },
    {
        "nome": "Gilson Filho",
        "email": "contatogilsonsbf@gmail.com",
        "twitter": "@gilsonfilho",
        "github": "gilsondev"
    },
    {
        "nome": "Dirley Rodrigues",
        "email": "N/A",
        "twitter": "@dirleyrls",
        "github": "ravishi"
    },
    {
        "nome": "Wagner Santos",
        "email": "wagnerjs.unb@gmail.com",
        "twitter": "@wagnerjsantos",
        "github": "wagnerjs"
    },
    {
        "nome": "Israel P. Siqueira",
        "email": "israelps@gmail.com",
        "twitter": "@israelps",
        "github": "israelps"
    },
    {
            "nome": "Magnun Leno",
            "email": "magnun.leno@gmail.com",
            "twitter": "@mind_bend",
            "github": "magnunleno",
            "site": {
                "nome": "Mind Bending",
                "href": "http://mindbending.org",
                }
    }
)
