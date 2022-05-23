# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Need to add packages here if the Autodoc extension is used
# See http://blog.rtwilson.com/how-to-make-your-sphinx-documentation-compile-with-readthedocs-when-youre-using-numpy-and-scipy/
import mock

MOCK_MODULES = ['numpy', 'tables', 'matplotlib','matplotlib.pyplot','matplotlib.ticker', 'matplotlib.colors']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

sys.path.insert(0, os.path.abspath('../../tolip'))
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'ToLiP'
copyright = '2022, Suyash Bhattarai'
author = 'Suyash Bhattarai'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
             'sphinx_rtd_theme',
             'numpydoc'
]

#autodoc_default_options = {"autosummary": True}
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# This prevents sphinx from printing full path
# Instead of x.y.z.fun(), it will just print func() 
add_module_names = False


