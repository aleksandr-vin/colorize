Highlight matched strings in a text
===================================

.. image:: https://asciinema.org/a/fYZQYgtftLeicD4ap4zMHveg6.png
  :width: 400
  :alt: Showcase

`See in action <https://asciinema.org/a/fYZQYgtftLeicD4ap4zMHveg6>`_

Usage
-----

Pipe text though it to highlight:

1. Numbers, try::

    cat something | colorize '[0-9]+'

2. Lines matching phrase, try::

    cat anotherthing | colorize '.*phrase.*'

3. Headers in curl, try::

    cat anything | colorize '^[^:]*:'

If you don't like distribution of the colors, add some random number as second argument.

Installation
------------

You can install via brew::

    brew install aleksandr-vin/taps/colorize-cli
    
or pypi::

    pip install colorize-cli
