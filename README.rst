dev-pipeline
============
|codacy|
|code-climate|
|lgtm|
|lgtm-quality|

A tool to help manage projects with dependencies spread across repositories.


Inspiration
-----------
I work on several projects spread across repositories; some of these leverage
sub-repositories in some form, and it's led to additional complexity trying to
stay in sync (especially when dealing with merges, release lines, hot fixes,
and all the other fun things that happen in large software projects).  The
goal here is to have a suite of scripts to help keep repositories in sync and
working well together, without the issues that sub-repositories introduce.


Installation
------------
Requirements
~~~~~~~~~~~~
dev-pipeline requires python3; python2 will not work.


From PyPi
~~~~~~~~~
If a published version is good enough, you can install using pip_.  PyPi_ has
all published versions, including alpha and beta releases.

.. code:: bash

    $ pip3 install dev-pipeline


From Source
~~~~~~~~~~~
If the version in PyPi_ isn't recent enough, you can install directoy from
source using pip_.  Because dev-pipeline is spread across several repositories
(each tool and plugin is tracked separately), you'll need to install all of
them as well (see their documentation).  Dependencies are listed in
`setup.py`_.

.. code:: bash

    $ cd /path/to/dev-pipeline
    $ pip3 install

If you don't have pip available, you can run :code:`setup.py` directly.

.. code:: bash

    $ cd /path/to/dev-pipeline
    $ python3 setup.py install

If the install completes without errors, then you're good to go.


Using
-----
The first thing you'll need to do is write a `build configuration`_.  Once
you're ready, a build directory.

.. code:: bash

    # configure with default settings
    $ dev-pipeline configure

If everything went well, you're ready to build.

.. code:: bash

    # enter whatever directory the configure step used
    $ cd build
    # bootstrap will both pull the package sources and build them
    $ dev-pipeline bootstrap

That's it.  Check the tool documentation for information on what's available.


.. |codacy| image:: https://api.codacy.com/project/badge/Grade/0d9cf1d52ca846dc99de6cc621dfeb7b
    :target: https://www.codacy.com/app/snewell/dev-pipeline?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-pipeline/dev-pipeline&amp;utm_campaign=Badge_Grade
.. |code-climate| image:: https://api.codeclimate.com/v1/badges/9427722fafe270b6716f/maintainability
   :target: https://codeclimate.com/github/dev-pipeline/dev-pipeline/maintainability
   :alt: Maintainability
.. |lgtm| image:: https://img.shields.io/lgtm/alerts/g/dev-pipeline/dev-pipeline.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/dev-pipeline/dev-pipeline/alerts/
.. |lgtm-quality| image:: https://img.shields.io/lgtm/grade/python/g/dev-pipeline/dev-pipeline.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/dev-pipeline/dev-pipeline/context:python

.. _build configuration: docs/config.rst
.. _pip: https://pypi.python.org/pypi/pip
.. _PyPi: https://pypi.org/project/dev-pipeline/
.. _setup.py: https://github.com/dev-pipeline/dev-pipeline/blob/master/setup.py
