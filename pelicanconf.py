#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.curdir)

from collections import OrderedDict

AUTHOR = u'Grupy-DF'
SITENAME = u'Grupy-DF'
SITEURL = ''

META_DESCRIPTION = '''O Grupy-DF é uma comunidade de usuários (profissionais e
                      amadores) da linguagem Python, onde prezamos pela troca de
                      conhecimento, respeito mútuo e diversidade (tanto de opinião
                      quanto de tecnologias).'''

META_KEYWORDS = ['grupy-df', 'python', 'brasilia', 'desenvolvimento']

TIMEZONE = 'America/Sao_Paulo'
THEME = 'themes/malt'
MALT_BASE_COLOR = 'green'

SITE_LOGO = 'images/logo/logo.png'
SITE_LOGO_MOBILE = 'images/logo/logo-inv.png'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

WELCOME_TITLE = 'Seja bem vindo ao {}!'.format(SITENAME)
WELCOME_TEXT = 'Grupo de usuários da linguagem Python no Distrito Federal.'
SITE_BACKGROUND_IMAGE = 'images/banners/ponte-jk.jpg'
FOOTER_ABOUT = '''O Grupy-DF é uma comunidade de usuários (profissionais e
                  amadores) da linguagem Python, onde prezamos pela troca de
                  conhecimento, respeito mútuo e diversidade (tanto de opinião
                  quanto de tecnologias).'''

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

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
    'better_figures_and_images',
    'sitemap',
]

RESPONSIVE_IMAGES = True
PYGMENTS_STYLE = "perldoc"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

GITHUB_REPO = "http://github.com/grupydf/grupydf.github.io"
GITHUB_BRANCH = "pelican"
TWITTER = "@grupydf"
OPEN_GRAPH_IMAGE = "/images/logo/logo-inv.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title": "Comunidade",
        "href": "comunidade",
    },
    {
        "title": "Membros",
        "href": "membros",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

SOCIAL_LINKS = (
    {
        "href": "https://telegram.me/joinchat/AG9QCABLx9wgYM1bcoGxgQ",
        "icon": "fa-paper-plane",
        "text": "Telegram",
    },
    {
        "href": "https://github.com/grupydf",
        "icon": "fa-github",
        "text": "GitHub",
    },
    {
        "href": "https://twitter.com/grupydf",
        "icon": "fa-twitter",
        "text": "Twitter",
    },
    {
        "href": "https://www.facebook.com/groups/grupydf",
        "icon": "fa-facebook",
        "text": "Facebook",
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
    ("Bleno", {
        "email": "blenobok@gmail.com",
        "twitter": "@blenobok",
        "github": "bleno"
        }),
    ("Bruno Barbosa", {
        "email": "bsbruno1@gmail.com",
        "twitter": "@brunobbbs",
        "github": "brunobbbs",
        "site": {
            "nome": "Anotações de um programador Python",
            "href": "http://brunobarbosa.com.br",
            }
        }),
    ("Dirley Rodrigues", {
        "twitter": "@dirleyrls",
        "github": "ravishi"
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
    ("Gilson Filho", {
        "email": "me@gilsondev.in",
        "twitter": "@gilsonfilho",
        "github": "gilsondev"
        }),
    ("Humberto Rocha", {
        "email": "humrochagf@gmail.com",
        "twitter": "@humrochagf",
        "github": "humrochagf"
        }),
    ("Israel P. Siqueira", {
        "email": "israelps@gmail.com",
        "twitter": "@israelps",
        "github": "israelps"
        }),
    ("Jéssica Macedo", {
        "email": "jessica.mmacedo@gmail.com",
        "twitter": "@jemmacedo",
        "github": "jornalistadigital"
        }),  
    ("Magnun Leno", {
        "email": "magnun.leno@gmail.com",
        "twitter": "@mind_bend",
        "github": "magnunleno",
        "site": {
            "nome": "Mind Bending",
            "href": "http://mindbending.org",
            }
        }),    
    ("Marco Rougeth", {
        "email": "marco@rougeth.com",
        "twitter": "@marcorougeth",
        "github": "rougeth"
        }),
    ("Mário Sérgio", {
        "email": "sergio.mario_q@hotmail.com",
        "twitter": "@queirozMario21",
        "github": "sergiomario"
        }),
    ("Pedro Henrique", {
        "email": "pedrohenriqueacruz@gmail.com",
        "twitter": "@phinfonet",
        "github": "phinfonet"
        }),
    ("Tânia Andrea", {
        "email": "taniaa.moreira@gmail.com",
        "twitter": "@taniaandrea_com",
        "github": "taniaa",
        "site": {
            "nome": "Meu perfil hacker :)",
            "href": "http://calango.club/membros/taniaa",
            }      
        }),  
    ("Wagner Santos", {
        "email": "wagnerjs.unb@gmail.com",
        "twitter": "@wagnerjsantos",
        "github": "wagnerjs"
        })
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A comunidade do GrupyDF se comunica através de mailing " +\
                    "lists e do grupo no telegram mas frequentemente são " +\
                    "promovidos encontros diversos, como almoços, " +\
                    "<em>coding dojos</em> e palestras. ",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade do GrupyDF, apesar de extensa possui alguns " +\
                        "colaboradores principais, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": " Atualmente o GrupyDF possui poucos projetos em andamento:" +\
                        "Traduções do Django-docs e Python on Campus.",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "projetos",
                    },
                ],
            },
        ]
    },
]

from themes.malt.functions import *
