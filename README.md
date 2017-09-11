# oTree-fishery

This is a fork of (otree-core)[https://github.com/oTree-org/otree-core] which is customized for the fishery simulator game.

## References from the main repo


Docs
----

http://otree.readthedocs.io/en/latest/index.html


Core dev setup
~~~~~~~~~~~~~~

If you are modifying otree-core locally, clone or download this repo,
then run this from the project root:

::

    pip install -e .
    cd .. # or wherever you will start your project
    otree startproject oTree
    otree resetdb
    otree runserver

See `this`_ document that explains how oTree differs from a typical
Django project.

|Build Status|

.. _Homepage: http://www.otree.org/
.. _this: http://otree.readthedocs.io/en/latest/django.html

.. |Build Status| image:: https://travis-ci.org/oTree-org/otree-core.svg?branch=master
   :target: https://travis-ci.org/oTree-org/otree-core
