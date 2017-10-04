.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/arekstasiewicz/ckanext-rtpa_theme.svg?branch=master
    :target: https://travis-ci.org/arekstasiewicz/ckanext-rtpa_theme

.. image:: https://coveralls.io/repos/arekstasiewicz/ckanext-rtpa_theme/badge.png?branch=master
  :target: https://coveralls.io/r/arekstasiewicz/ckanext-rtpa_theme?branch=master

.. image:: https://pypip.in/download/ckanext-rtpa_theme/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-rtpa_theme/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-rtpa_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-rtpa_theme/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-rtpa_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-rtpa_theme/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-rtpa_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-rtpa_theme/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-rtpa_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-rtpa_theme/
    :alt: License

=============
ckanext-rtpa_theme
=============

Rtpa_Theme is a graphical overlay for ckan platform - it makes it look like RouteToPA Project (link :http://vmegov01.deri.ie/en). 




------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-rtpa_theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Import repository from github.com::

    git clone https://github.com/routetopa/ckanext-rtpa_theme.git
    cd ckanext-rtpa_theme
    python setup.py develop

3. Add ``rtpa_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

   ``sudo service apache2 reload``
     
5. Start CKAN environment::

   ``paster serve /etc/ckan/default/development.ini``



-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.rtpa_theme --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-rtpa_theme on PyPI
---------------------------------

ckanext-rtpa_theme should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-rtpa_theme. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-rtpa_theme
----------------------------------------

ckanext-rtpa_theme is availabe on PyPI as https://pypi.python.org/pypi/ckanext-rtpa_theme.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
