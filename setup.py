from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Translate Amharic that written in english to Amharic characters'
# Setting up
setup(
    name="fidel",
    version=VERSION,
    author="Neftalem Yeneneh",
    author_email="n.y.official.em@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["symspellpy == 6.7.1" ,"googletrans == 4.0.0-rc1"],
    keywords=['python', 'amharic', 'amharic to english', 'ethiopia', 'translate', 'fidel']
)
