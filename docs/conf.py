# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_material
import os
import sys
import subprocess
import shutil

# Add the path to your module folder
sys.path.insert(0, os.path.abspath('..'))

project = 'Universal Upgrade Library Python'
copyright = '2023, lpawlick'
author = 'lpawlick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx"]
autodoc_typehints = "both"
exclude_patterns = []

# Configuration for intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.11', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
html_title = "Universal Upgrade Library Python"
html_sidebars = {
    '**': [ 'about.html',
            'postcard.html', 'navigation.html',
            'recentposts.html', 'tagcloud.html',
            'categories.html',  'archives.html',
            'searchbox.html', #'logo-text.html',
            'globaltoc.html', #'localtoc.html'
            ],
    }
html_theme_options = {
    #'touch_icon' : '',
    'base_url' : '/',
    'globaltoc_depth' : -1,
    'theme_color' : '5F021F',
    'color_primary' : 'red',
    'color_accent' : 'red',
    #'html_minify' : True,
    'css_minify' : True,
    #'logo_icon' : '',
}

# Define the location of the parent directory
parent_directory = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Build the wheel using pip wheel
subprocess.run(["pip", "wheel", parent_directory, "-w", os.path.join(parent_directory, "_build", "pages")])

# List of example files to copy
example_files = ["content.py", "index.css"]

# Copy example files from the parent directory to the Sphinx build directory
for example_file in example_files:
    example_src_path = os.path.join(parent_directory, "examples", "browser", example_file)
    example_dest_path = os.path.join(parent_directory, "_build", "pages", example_file)
    shutil.copy(example_src_path, example_dest_path)
