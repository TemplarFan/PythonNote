from distutils.core import setup, Extension

mod = "exttest"

module1 = Extension(mod, sources=["exttest.c"])

setup(
    name="fib",
    version="1.0",
    description="test",
    author="wei",
    ext_modules= [module1]
)