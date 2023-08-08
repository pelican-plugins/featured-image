Featured Image: A Plugin for Pelican
====================================

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/featured-image/main.yml?branch=main)](https://github.com/pelican-plugins/featured-image/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-featured-image)](https://pypi.org/project/pelican-featured-image/)
[![Downloads](https://img.shields.io/pypi/dm/pelican-featured-image)](https://pypi.org/project/pelican-featured-image/)
![License](https://img.shields.io/pypi/l/pelican-featured-image?color=blue)

This Pelican plugin extracts an image from the summary or content of an article or page if not already specified in content metadata.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-featured-image

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `featured_image` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

Usage
-----

To override the default behavior of selecting the first image in the article's summary or content, set the image property the article's metadata to the URL of the image to display, e.g:

```markdown
Title: My super title
Date: 2010-12-03 10:20
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Author: Alexis Metaireau
Summary: Short version for index and feeds
Image: /images/my-super-image.png

Article content...
```

### Page

To include a representative image in a page add the following to the template:

```html
{% if page.featured_image %}
    <img src="{{ page.featured_image }}">
{% endif %}
```

### Article

To include a representative image in an article add the following to the template:

```html
{% if article.featured_image %}
    <img src="{{ article.featured_image }}">
{% endif %}
```

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/featured-image/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the AGPL-3.0 license.
