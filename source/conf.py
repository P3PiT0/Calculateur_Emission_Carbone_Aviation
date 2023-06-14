# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Calculateur_Emission_Carbone_Aviation'
copyright = '2023, Lucas Chamaz <lucas.chamaz.1@ens.etsmtl.ca> ; Alexandre Panhaleux <alenxandre.panhaleux.1@ens.etsmtl.ca> ; Étienne Lionnet <etienne.lionnet.1@ens.etsmtl.ca> ; Gabriel Gunther <gabriel.gunther.1@ens.etsmtl.ca>'
author = 'Lucas Chamaz <lucas.chamaz.1@ens.etsmtl.ca> ; Alexandre Panhaleux <alenxandre.panhaleux.1@ens.etsmtl.ca> ; Étienne Lionnet <etienne.lionnet.1@ens.etsmtl.ca> ; Gabriel Gunther <gabriel.gunther.1@ens.etsmtl.ca>'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath("../"))
#sys.path.insert(0, os.path.abspath("../other_code"))

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions = ["sphinx.ext.autodoc"]

html_theme = 'alabaster'
html_static_path = ['_static']
