#setup.py

from setuptools import setup, find_packages

from Cython.Build import cythonize

setup(name="mx",
      ext_modules=cythonize("mx.py")
     )