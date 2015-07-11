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
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

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
NAVBAR_HOME_LINKS = [
    {
        "title" : "Membros",
        "href": "membros",
    },
    {
        "title" : "Blog",
        "href": "blog",
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title" : "Categorias",
        "href": "blog/categorias",
    },
    {
        "title" : "Autores",
        "href": "blog/autores",
    },
    {
        "title" : "Tags",
        "href": "blog/tags",
    },
]

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

import os
import random
import functools
from md5 import md5

def GET_AVATAR(autor):
    if autor in MEMBROS:
        if 'github' in MEMBROS[autor]:
            formatter = "https://avatars.githubusercontent.com/{}?size=250"
            username = MEMBROS[autor]['github']
        elif 'email' in MEMBROS[autor]:
            formatter = "http://www.gravatar.com/avatar/{}?s=250"
            username = md5(MEMBROS[autor]['email'].strip().lower()).hexdigest()
        elif 'twitter' in MEMBROS[autor]:
            formatter = "http://avatars.io/twitter/{}"
            username = MEMBROS[autor]['twitter']
            if username.startswith("@"):
                username = username[1:]
        else:
            formatter = "/theme/img/{}"
            username = "default_avatar.png"
    else:
        formatter = "/theme/img/{}"
        username = "default_avatar.gif"
    return formatter.format(username)

def GET_ARTICLE_IMAGE(article):
    if hasattr(article, 'image'):
        return article.image

    root = os.path.join(THEME, "static", "img", "banners")
    base = "/theme/img/banners"
    banners = map(functools.partial(os.path.join, base), os.walk(root).next()[2])
    random.seed(article.date)
    return random.choice(banners)

def GET_ARTICLE_AT_GITHUB(article):
    base = os.path.relpath(article.source_path, os.getcwd())
    url = "https://github.com/grupydf/grupydf.github.io/tree/pelican/{}"
    return url.format(base)
