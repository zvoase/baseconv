from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

def readfile(filename):
    fp = open(filename)
    try:
        data = fp.read()
    except:
        raise
    finally:
        fp.close()
    return data

setup(
    name='BaseConv',
    version='0.1a',
    description='A generic base-conversion library for Python.',
    long_description=readfile('README.rst'),
    license=readfile('LICENSE'),
    author='Zachary Voase',
    author_email='zack@biga.mp',
    url='http://github.com/zvoase/baseconv/tree/master',
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    exclude_package_data={'': ['README.textile', 'README.rst', 'LICENSE']}
)