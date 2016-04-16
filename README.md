# SkyWiki
SkyWiki is a simple flat-page wiki based on Django. Pages are written in Markdown
and then compiled in HTML via Python. This permit to finally enjoy writting wiki
pages like never before.

Note that this is still a work in progress and it's subject to change **a lot**
before a stable version will be released.

## Requirements
SkyWiki depends on very minimal dependencies. Here is the list of what you'll
need to install before being able to run your very own wiki:

* django   `>=1.8.11`
* markdown `>=2.6.6`
* py-gfm   `>=0.1.2`

## Installation
In order to install **SkyWiki** you need to have installed `python2.7` and `pip`.  
If all is correctly installed, you should just have to run the following:

```sh
git clone https://github.com/SkyzohKey/SkyWiki.git
cd SkyWiki
pip install -r requirements.txt
```

## Config
You can configure SkyWiki a little bit yet, but that's going to be something you
can fully customize in a near future ;)

Configuration file is located in `$project_root/wiki/config.py`.  
Here are the main key you can change with a little explaination about their usage.

* `WIKI_TITLE`: The title of your wiki.
* `WIKI_GITHUB`: The GitHub link to your wiki.

## Creating a page
SkyWiki use a simple folder system to enable categories.  
Pages are located in `$project_root/wiki/content/`.

In order to create a category, simply make a folder with the category name.  
In order to create a page, navigate to the folder you want to use and create a
file following this pattern: `$page_name.md`.

Pages are storing some meta-data at the top. SkyWiki currently only need a `title`
meta to display the title of the page in your browser. But their is also 2 more
meta-tags you can use ; `author` and `date` (a UNIX timestamp).

Let's have a look at a basic page file.

`$page_name.md` :
```md
---
title: My super page title
author: SkyzohKey
date: 1460729559
---

# This is a super cool page
All of what you write here **must** be in Markdown.  
No _HTML_ is allowed! Ofc, Markdown beats HTML.
```

## Running the wiki server
Starting the wiki server is taking only 1 command, you can even choose the port
you want to run in. The following commands needs to be ran in `$project_root`.

```sh
# Simply start the server on 127.0.0.1:8000
./manage.py runserver

# Start the server on the port 80
./manage.py runserver 80

# Start the server on 0.0.0.0:80 to allow external access
./manage.py runserver 0.0.0.0:80
```

Once server is starter, you never more have to stop it. Add your pages and
enjoy the true simplicity of a SkyWiki!

Enjoy!  
