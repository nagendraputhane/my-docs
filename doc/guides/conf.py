import python_docs_theme

project = 'my-docs'
copyright = '2025, nagendra'
author = 'nagendra'
release = '0.0.1'
master_doc = 'index'
html_logo = 'logo/logo.jpg'

# You don't need autodoc/extensions now
extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "python_docs_theme"
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]
html_js_files = [
    'js/titleprefix.js',
]

html_title = ""

# Sidebar with dropdowns + prev/next buttons
html_sidebars = {
    "**": [
        "globaltoc.html",    # sidebar with collapsible sections
        "relations.html",    # prev/next buttons
        "searchbox.html",    # search bar
    ]
}

html_context = {
    "project": "DAO",
    "project_copyright": "© 2025 Marvell",
    "default_mode": "light",  # if using dark mode switch
}
