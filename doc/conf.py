# -*- coding: utf-8 -*-
#
# Apache Traffic Server documentation build configuration file, created by
# sphinx-quickstart on Mon Mar  4 06:23:15 2013.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('ext'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.mathjax', 'sphinx.ext.viewcode', 'traffic-server' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Apache Traffic Server'
copyright = u'2013, dev@trafficserver.apache.org'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '4.0'
# The full version, including alpha/beta/rc tags.
release = '4.0.x'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'agogo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'static/images/trans_logo_tm_380x69.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'static/images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'ApacheTrafficServerdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'ApacheTrafficServer.tex', u'Apache Traffic Server Documentation',
   u'dev@trafficserver.apache.org', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [

   ('reference/api/TSAPI.en', 'TSAPI', u'Introduction to the Apache Traffic Server API', None, u'3ts'),
   ('reference/api/TSDebug.en', 'TSDebug', u'Traffic Server Debugging APIs', None, u'3ts'),
   ('reference/api/TSHttpHookAdd.en', 'TSHttpHookAdd', u'Intercept Traffic Server events', None, u'3ts'),
   ('reference/api/TSHttpParserCreate.en', 'TSHttpParserCreate', u'Parse HTTP headers from memory buffers', None, u'3ts'),
   ('reference/api/TSHttpTxnMilestoneGet.en', 'TSHttpTxnMilestoneGet', u'Get a specified milestone timer value for the current transaction', None, u'3ts'),
   ('reference/api/TSIOBufferCreate.en', 'TSIOBufferCreate', u'Traffic Server IO buffer API', None, u'3ts'),
   ('reference/api/TSInstallDirGet.en', 'TSInstallDirGet', u'Return Traffic Server installation directories', None, u'3ts'),
   ('reference/api/TSMBufferCreate.en', 'TSMBufferCreate', u'Traffic Server marshall buffer API', None, u'3ts'),
   ('reference/api/TSmalloc.en', 'TSmalloc', u'Traffic Server memory allocation API', None, u'3ts'),
   ('reference/api/TSPluginInit.en', 'TSPluginInit', u'Traffic Server plugin loading and registration', None, u'3ts'),
   ('reference/api/TSRemap.en', 'TSRemap', u'Traffic Server remap plugin entry points ', None, u'3ts'),
   ('reference/api/TSTrafficServerVersionGet.en', 'TSTrafficServerVersionGet', u'return Traffic Server version information', None, u'3ts'),
   ('reference/api/TSUrlCreate.en', 'TSUrlCreate', u'Traffic Server URL manipulation API', None, u'3ts'),

   ('reference/commands/traffic_cop.en', 'traffic_cop', u'Traffic Server watchdog', None, '8'),
   ('reference/commands/traffic_line.en', 'traffic_line', u'Traffic Server command line', None, '8'),
   ('reference/commands/traffic_logcat.en', 'traffic_logcat', u'Traffic Server log spooler', None, '8'),
   ('reference/commands/traffic_logstats.en', 'traffic_logstats', u'Traffic Server analyzer', None, '8'),
   ('reference/commands/traffic_manager.en', 'traffic_manager', u'Traffic Server process manager', None, '8'),
   ('reference/commands/traffic_server.en', 'traffic_server', u'Traffic Server', None, '8'),
   ('reference/commands/traffic_shell.en', 'traffic_shell', u'Traffic Server shell', None, '8'),

   ('reference/commands/tspush.en', 'tspush', u'Push objects into the Traffic Server cache', None, '1'),
   ('reference/commands/tstop.en','tstop', u'Display Traffic Server statistics', None, '1'),
   ('reference/commands/tsxs.en', 'tsxs', u'Traffic Server plugin tool', None, '1'),

   ('reference/configuration/cache.config.en', 'cache.config', u'Traffic Server cache configuration file', None, '5'),
   ('reference/configuration/congestion.config.en', 'congestion.config', u'Traffic Server congestion control configuration file', None, '5'),
   ('reference/configuration/hosting.config.en', 'hosting.config', u'Traffic Server domain hosting configuration file', None, '5'),
   ('reference/configuration/icp.config.en', 'icp.config', u'Traffic Server ICP configuration file', None, '5'),
   ('reference/configuration/ip_allow.config.en', 'ip_allow.config', u'Traffic Server IP access control configuration file', None, '5'),
   ('reference/configuration/log_hosts.config.en', 'log_hosts.config', u'Traffic Server log host configuration file', None, '5'),
   ('reference/configuration/logs_xml.config.en', 'logs_xml.config', u'Traffic Server log format configuration file', None, '5'),
   ('reference/configuration/parent.config.en', 'parent.config', u'Traffic Server parent cache configuration file', None, '5'),
   ('reference/configuration/plugin.config.en', 'plugin.config', u'Traffic Server global plugin configuration file', None, '5'),
   ('reference/configuration/records.config.en', 'records.config', u'Traffic Server configuration file', None, '5'),
   ('reference/configuration/remap.config.en', 'remap.config', u'Traffic Server remap rules configuration file', None, '5'),
   ('reference/configuration/splitdns.config.en', 'splitdns.config', u'Traffic Server split DNS configuration file', None, '5'),
   ('reference/configuration/ssl_multicert.config.en', 'ssl_multicert.config', u'Traffic Server SSL certificate configuration file', None, '5'),
   ('reference/configuration/storage.config.en', 'storage.config', u'Traffic Server cache storage configuration file', None, '5'),
   ('reference/configuration/update.config.en', 'update.config', u'Traffic Server automated update configuration file', None, '5'),
   ('reference/configuration/volume.config.en', 'volume.config', u'Traffic Server cache volume configuration file', None, '5'),

]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'ApacheTrafficServer', u'Apache Traffic Server Documentation',
   u'dev@trafficserver.apache.org', 'ApacheTrafficServer', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Apache Traffic Server'
epub_author = u'dev@trafficserver.apache.org'
epub_publisher = u'dev@trafficserver.apache.org'
epub_copyright = u'2013, dev@trafficserver.apache.org'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True
