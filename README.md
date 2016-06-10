langdetect
==========

Port of Google's [language-detection](https://code.google.com/p/language-detection/) library (version from 03/03/2014) to Python.


Installation
============

    $ pip install langdetect

Supported Python versions 2.6, 2.7, 3.x.


Languages
=========

``langdetect`` supports 55 languages out of the box ([ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)):

    af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
    hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
    pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw


Basic usage
===========

To detect the language of the text:

```python
>>> from langdetect import detect
>>> detect("War doesn't show who's right, just who's left.")
'en'
>>> detect("Ein, zwei, drei, vier")
'de'
```

To find out the probabilities for the top languages:

```python
>>> from langdetect import detect_langs
>>> detect_langs("Otec matka syn.")
[sk:0.572770823327, pl:0.292872522702, cs:0.134356653968]
```

**NOTE**

Language detection algorithm is non-deterministic, which means that if you try to run it on a text which is either too short or too ambiguous, you might get different results everytime you run it.

To enforce consistent results, call following code before the first language detection:

```python
from langdetect import DetectorFactory
DetectorFactory.seed = 0
```

How to add new language?
========================

You need to create a new language profile. The easiest way to do it is to use the [langdetect.jar](https://github.com/shuyo/language-detection/raw/master/lib/langdetect.jar) tool, which can generate language profiles from Wikipedia abstract database files or plain text.

Wikipedia abstract database files can be retrieved from "Wikipedia Downloads" ([http://download.wikimedia.org/](http://download.wikimedia.org/)). They form '(language code)wiki-(version)-abstract.xml' (e.g. 'enwiki-20101004-abstract.xml' ).

usage: ``java -jar langdetect.jar --genprofile -d [directory path] [language codes]``

- Specify the directory which has abstract databases by -d option.
- This tool can handle gzip compressed file.

Remark: The database filename in Chinese is like 'zhwiki-(version)-abstract-zh-cn.xml' or zhwiki-(version)-abstract-zh-tw.xml', so that it must be modified 'zh-cnwiki-(version)-abstract.xml' or 'zh-twwiki-(version)-abstract.xml'.

To generate language profile from a plain text, use the genprofile-text command.

usage: ``java -jar langdetect.jar --genprofile-text -l [language code] [text file path]``

For more details see [language-detection Wiki](https://code.google.com/archive/p/language-detection/wikis/Tools.wiki).


Original project
================

This library is a direct port of Google's [language-detection](https://code.google.com/p/language-detection/) library from Java to Python. All the classes and methods are unchanged, so for more information see the project's website or wiki.

Presentation of the language detection algorithm: [http://www.slideshare.net/shuyo/language-detection-library-for-java](http://www.slideshare.net/shuyo/language-detection-library-for-java).
