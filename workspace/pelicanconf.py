#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mohammed EL BEIED'
SITENAME = u'blog for testng knowlodge'
SITEURL = 'https://melbeied.github.io'


SITESUBTITLE = '<pre>$ ^M ...</pre>'
SITEDESCRIPTION = u's programming, java, python, , iconcept, logic'
PATH = 'public'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
LOCALE = 'en_US.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('envelope', 'mailto:melbeied@gmail.com'),
        ('github', 'https://github.com/melbeied/'),)

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


OUTPUT_PATH = 'public/'
# Theme setting
THEME="/home/vagrant/pelican-themes/Flex/"
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'default'

STATIC_PATHS= [ 'pages', 'category']
MAIN_MENU= True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Blog', '/category/blog.html'),
    ('Documentation', 'http://docs.getpelican.com')

    )

