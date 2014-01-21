#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Watson - Events documentation build configuration file, created by
# sphinx-quickstart on Fri Jan 17 14:49:48 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import watson.events

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.napoleon'
]

templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

project = 'Watson - Events'
copyright = '2014, Simon Coulton'

version = watson.events.__version__
release = version

exclude_patterns = ['_build']

pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

htmlhelp_basename = 'Watson-Eventsdoc'

# html_sidebars = {}
html_show_sourcelink = False
html_show_sphinx = False


# -- Options for manual page output ---------------------------------------

man_pages = [
    ('index', 'watson-events', 'Watson - Events Documentation',
     ['Simon Coulton'], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    ('index', 'Watson-Events', 'Watson - Events Documentation',
     'Simon Coulton', 'Watson-Events', 'Trigger and handle event flow with your application.',
     'Miscellaneous'),
]

texinfo_appendices = []

# Intersphinx Mapping

# Autodoc


def skip(app, what, name, obj, skip, options):
    if name == '__init__':
        return False
    elif name in ('__module__', '__doc__', '__abstractmethods__'):
        return True
    return skip


def setup(app):
    app.connect('autodoc-skip-member', skip)
