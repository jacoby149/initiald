# Initial D

*A library that makes flat namespaces easy when designing python packages*

Layout python packages such that functions are called straight from the parent directories of the python files they exist in.

```
#__setup.py__ of your custom package

#as usual, import setup tools
import setuptools

#Importing this library
import initiald 

#directories that have a subdirectory tree to entirely flatten
flatten = [relative paths of directories to entirely flatten in production]

#directories and python files to exclude from user interfacing.
exclude = [relative paths of directories and python files to exclude from user interfacing]

#how it works
initiald.create_inits()  																								 # __now__

#Generate the correct __init.py__ files
#initiald.create_inits(flatten=flatten, exclude=exclude)     						# __future__

#install the custom package
setup(...)

```

