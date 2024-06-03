from setuptools import setup, Extension
from Cython.Build import cythonize
import os
import shutil

# Clean build directory and generated files
build_dirs = ['build', 'tngl/backends/hackrf.c', 'tngl/backends/hackrf_sweep.cpython-311-x86_64-linux-gnu.so']
for build_dir in build_dirs:
    if os.path.exists(build_dir):
        if os.path.isdir(build_dir):
            shutil.rmtree(build_dir)
        else:
            os.remove(build_dir)

extensions = [
    Extension(
        name="hackrf_sweep",
        sources=["tngl/backends/hackrf.pyx", "tngl/backends/hackrf_driver.c"],
        extra_compile_args=["-Wall"],
    )
]

setup(
    name="hackrf_sweep",
    ext_modules=cythonize(extensions, language_level="3", annotate=True),
)