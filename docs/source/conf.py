# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Clip-Zip-Ship (CZS) Documentation'
copyright = '2023, Natural resources Canada, His Majesty the King in right of Canada'
author = 'Natural resources Canada'

release = '0.1'
version = '0.1.0'

tls_verify = False

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'rst2pdf.pdfbuilder',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']


pdf_documents = [
    ('index', 'CZS_Documentation_en', 'CZS Documentation', 'Natural ressources Canada, Canada Centre for Mapping and Earth Observation, GeoDiscovery'),
]

templates_path = ['_templates']
locale_dirs = ['locale']
gettext_compact = False

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static'] 
html_favicon = 'media/geoca.png'
master_doc = 'index'

html_show_sphinx = True

html_theme_options = {
  'navigation_depth': 5,
  'collapse_navigation': False,
  'sticky_navigation': True,
  'display_version':False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file('cdtk.css')