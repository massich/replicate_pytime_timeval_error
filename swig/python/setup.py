
from skbuild import setup

setup(
    name="replicate_pytime_timeval_error",
    version="0.1",
    description="a minimal example package (cpp version)",
    author='The scikit-build team',
    license="MIT",
    packages=['replicate_pytime_timeval_error'],
    tests_require=[],
    setup_requires=[],
    cmake_args=['-DPYTHON_REL_SITE_ARCH:PATH=replicate_pytime_timeval_error'],
    cmake_source_dir="../../"
)
