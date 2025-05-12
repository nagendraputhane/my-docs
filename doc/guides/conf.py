import sphinx_rtd_theme

project = 'my-docs'
copyright = '2025, nagendra'
author = 'nagendra'
html_logo = 'logo/logo.jpg'
release = '0.0.1'
master_doc = 'index'

extensions = []

#templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]
