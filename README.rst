What is baseconv?
=================

baseconv is a generic *base* *conversion* library for Python. It allows you to
convert any number between binary, hexadecimal, decimal, octal or any other
base you can define. A base is a method of representing numbers; using two or
more different *words* you can represent any conceivable number using an
ordered combination of those words. For example, the *decimal* base is made up
of 10 words: 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9. *Binary* uses only 0 and 1.

Usage
=====

Installation
------------

To install baseconv, simply pull the repository using ``git`` (for more info
consult the `github documentation <http://github.com/guides>`_), ``cd`` into
the directory and run the following command as root:

	python setup.py install

This will copy ``baseconv.py`` to Python's ``site-packages`` directory, and
you can then import the library in your code via ``import baseconv``.

Using the Library In Your Code
------------------------------

In order to carry out the most common features of base conversion, the library
comes equipped with the pre-defined bases ``DECIMAL``, ``BINARY``,
``HEXADECIMAL``, ``OCTAL``, ``ALPHA_LOWER``, ``ALPHA_UPPER`` and ``ALPHA``.
This means you can, out of the box, convert between all of these bases. An
example usage case is shown below; note that numbers are held as instances of
the ``baseconv.Number`` class, and bases as ``baseconv.Base`` instances. The
attributes ``decimal``, ``base``, ``values`` and ``indices`` are all Python
*descriptors*; setting or otherwise changing one will cause the number's other
attributes to update. The following code sample shows how you might use the
library in a basic way:

	>>> from baseconv import *
	>>> num = BINARY('1010011010') # Create a number
	>>> num # Show the representation of a number
	Number(BINARY, '1010011010')
	>>> num.decimal
	666
	>>> num.decimal = 423 # Change a number's decimal value
	>>> num # The number's binary value has changed automatically
	Number(BINARY, '110100111')
	>>> num.base = HEXADECIMAL # Change a number's base
	>>> num
	Number(HEXADECIMAL, '1A7')
	>>> print num # Print a number as a string; also accessible via str(num)
	0x1A7
	>>> num.values # The sequence of base-words that this number represents
	'1A7'
	>>> num.values = 'FFC0DE' # Set this numbers values list
	>>> num # Number has changed accordingly
	Number(HEXADECIMAL, 'FFC0DE')
	>>> num.indices # The decimal value of each word in this number
	[15, 15, 12, 0, 13, 14]
	>>> num.indices = [1, 10, 7] # Set this number's indices attribute
	>>> num
	Number(HEXADECIMAL, '1A7')

About the Author
================

My name is Zachary Voase, and you can get to my personal home page (which has links to all my other pages) `here <http://biga.mp>`_.