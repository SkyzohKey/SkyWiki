# coding=utf-8
import os, os.path
import markdown

from django.shortcuts import render
from django.http import HttpResponse

# Github Flavored Markdown provided by `py-gfm`
from mdx_gfm import GithubFlavoredMarkdownExtension
from markdown.extensions.toc import TocExtension

WIKI_TITLE   = 'ToxWiki'
WIKI_GITHUB  = 'https://github.com/SkyzohKey/SkyWiki'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

PAGES_PATH       = os.path.join(PROJECT_ROOT, 'content')
ERROR_PAGES_PATH = os.path.join(PROJECT_ROOT, 'content', '_errors')

def __crawl(category = None, page = None):
    """
    This method is used to determine which page to load.
    It's main and only purpose is to return the correct path to the file.
    """

    if category == None and page == None:
        # Index page.
        path = os.path.join(PAGES_PATH, 'index.md')
    elif category == None and page != None:
        # Standalone page.
        path = os.path.join(PAGES_PATH, '%s.md' % page)
    elif category != None and page == None:
        # Categorized index page.
        path = os.path.join(PAGES_PATH, category, 'index.md' % page)
    else:
        # Categorized page.
        path = os.path.join(PAGES_PATH, category, '%s.md' % page)

    if os.path.exists(path):
        return path
    else:
        return os.path.join(ERROR_PAGES_PATH, '404.md')

def __parseMarkdown(path):
    """
    This method is in charge to open, read and parse the file at `path`.
    It then return the parsed result (Markdown → HTML)
    """

    # Initialize the Markdown parser:
    md = markdown.Markdown(extensions=[
        'meta',
        'markdown.extensions.tables',
        'markdown.extensions.tables',
        'markdown.extensions.extra',
        'markdown.extensions.smarty',
        GithubFlavoredMarkdownExtension(),
        TocExtension(anchorlink=True, permalink=True),
    ])

    # Open the file and read it, then parse:
    html   = open(path, 'r').read()
    result = md.convert(html)

    # Return the Markdown in HTML format:
    return (result, md)

def __renderView(request, md, html):
    """
    This method is meant to return the correct page with correct layout.
    """

    title  = md.Meta.get('title')[0].encode('utf-8')
    toc    = md.toc

    context = {
        'wiki': {
            'title' : WIKI_TITLE,
            'github': WIKI_GITHUB
        },
        'page': {
            'title': title,
        },
        'article': {
            'toc'    : toc,
            'content': html
        }
    }

    # If we have an author meta, let's pass it to the context.
    author = md.Meta.get('author')
    if author != None:
        context['page']['author'] = author[0].encode('utf-8')

    # If we have a date meta, let's pass it to the context.
    date = md.Meta.get('date')
    if date != None:
        context['page']['date'] = date[0].encode('utf-8')

    return render(request, 'wiki/layout.html', context)

def index(request):
    path     = __crawl(None, None)
    html, md = __parseMarkdown(path)
    return __renderView(request, md, html)

def standalonePage(request, page):
    path     = __crawl(None, page)
    html, md = __parseMarkdown(path)
    return __renderView(request, md, html)

def categorizedPage(request, category, page):
    path     = __crawl(category, page)
    html, md = __parseMarkdown(path)
    return __renderView(request, md, html)
