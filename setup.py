from setuptools import setup
import os


def read(fname):
    """Auxiliary function to read file from current folder."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='package',
      version='1.1',
      description=('Short description of your package.'),
      url='https://github.com/fwitte/python_example_repo',
      author='Francesco Witte',
      author_email='pythonkurs@witte.sh',
      long_description=read('README.rst'),
      license='GPL-3.0',
      packages=['package'],
      python_requires='>=3',
      install_requires=['numpy >= 1.14.3',
                        'pandas >= 0.22.0'])
