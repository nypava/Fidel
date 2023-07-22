from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.8'
DESCRIPTION = 'Python package that can change Amharic language that written in English alphabet to Amharic alphabet character.'

setup(
    name="fidel",
    version=VERSION,
    author="Niftalem Yeneneh",
    author_email="ny.dev0.em@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=['fidel'],
    package_dir={'': 'src'},
    package_data={'': ['data/*.txt']},
    install_requires=["symspellpy == 6.7.1" ],
    keywords=['python', 'amharic', 'english to amharic', 'ethiopia', 'translate', 'fidel']
)
