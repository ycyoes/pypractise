from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = Extension(
    "demo",
    ["demo.pyx"],
)

setup(
    ext_modules = cythonize([extension])
)


# execute this file through cmd:
#python setup.py build_ext --inplace

