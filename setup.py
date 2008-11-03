from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

fp = open('README.textile')
try:
    long_desc = fp.read()
except:
    raise
finally:
    fp.close()

setup(
    name='BaseConv',
    version='0.1a',
    description='A generic base-conversion library for Python.',
    long_description=long_desc,
    author='Zachary Voase',
    author_email='zack@biga.mp',
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    exclude_package_data={'': ['README.textile', 'LICENSE']}
)