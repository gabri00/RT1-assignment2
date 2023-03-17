# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RT assignment 2'
copyright = '2023, Gabriele Nicchiarelli'
author = 'Gabriele Nicchiarelli'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

extensions = [
   'sphinx.ext.autodoc',
   'sphinx.ext.intersphinx',
   'sphinx.ext.viewcode',
   'sphinx.ext.doctest',
   'sphinx.ext.githubpages',
   'sphinx.ext.napoleon',
   'sphinx.ext.viewcode'
]

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}