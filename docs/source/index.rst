.. Personal Productivity File Format documentation master file, created by
   sphinx-quickstart on Sun Jun  5 19:36:50 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dotprod (.prod) - Personal Productivity File Format
===================================================
.. warning::

    Dotprod is still a work in progress. In this stage, backwards compatability
    is not guaranteed and versioning in not maintained.

Dotprod is a personal productivity file format. Dotprod is based on JSON and is
meant to be a generic and standardized way to represent personal productivity
information - such as tasks, routines, ideas and more.

Dotprod is designed to support various personal productivity doctrines - from
a simple "to do" list to Getting Things Done.

It is our hope that providers of productivity apps will allow their users to
export and import their data using Dotprod.

"Dotprod" simply reads outs ".prod", which is the format's primary suggested
file extension.

Dotprod provides a JSON schema to allow productivity app providers a quick way
to verify that they are up to standard.

A minimal example
-----------------

.. literalinclude:: examples/positive/minimal_task.prod
   :language: json

Contents:

..
.. toctree::
   :maxdepth: 2
   :glob:

   examples


Indices and tables
==================

 * :ref:`genindex`
 * :ref:`modindex`
 * :ref:`search`



