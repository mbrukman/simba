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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'simba'
copyright = '2020, Joe Bentley'
author = 'Joe Bentley'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    # 'sphinx.ext.linkcode',
    'sphinx.ext.viewcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# allow sphinx to import the module
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# imgmath settings
imgmath_image_format = 'svg'
imgmath_font_size = 14
imgmath_latex_preamble = r"\usepackage{amssymb}"

# autodoc settings
autodoc_member_order = 'bysource'

# set the default role
default_role = 'any'

# make sure that we don't skip documenting these special cases
do_not_skip = ["__eq__", "__iter__", "__str__"]


def skip(app, what, name, obj, would_skip, options):
    if name in do_not_skip:
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


# def linkcode_resolve(domain, info):
#     if domain != 'py':
#         return None
#     if not info['module']:
#         return None
#     filename = info['module'].replace('.', '/')
#     print(info)
#     return f"https://github.com/joebentley/simba/tree/master/{filename}.py"
