""" 
Configuration file for the Sphinx documentation builder.
"""

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

PROJECT = 'DEPART'
COPYRIGHT = 'Patrick Capaldo, Kaixin Wang, Delaney Stevens, and Claudia de la Paz'
AUTHOR = 'Patrick Capaldo, Kaixin Wang, Delaney Stevens, and Claudia de la Paz'
RELEASE = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme must be lower case to be recognised by Sphinx
html_theme = 'sphinx_rtd_theme' # pylint: disable=invalid-name
HTML_STATIC_PATH = ['_static']
# Prevent "Built with Sphinx using a theme provided by Read the Docs." from showing
HTML_SHOW_SPHINX = False
