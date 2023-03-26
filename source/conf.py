# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../'))

project = 'RT assignment 2'
copyright = '2023, Gabriele Nicchiarelli'
author = 'Gabriele Nicchiarelli'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

highlight_language = 'python3'
source_suffix = '.rst'
master_doc = 'index'

html_theme = 'classic'
html_static_path = ['_static']

intersphinx_mapping = { 'python': ('https://docs.python.org/3', None) }

# -- Breathe configuration ---------------------------------------------------

# breathe_projects = { "RT assignment 2": "../build/xml/" }
# breathe_default_project = "RT assignment 2"
# breathe_default_members = ('members', 'undoc-members')
