# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'geopedestrian'
copyright = '2024, Geospatial AI'
author = 'Jan Tschada'

release = '0.3'
version = '0.3'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx'
    #'enum_tools.autoenum',
]

# Turn on sphinx.ext.autosummary
autosummary_generate = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'