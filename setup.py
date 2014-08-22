# -*- coding: utf-8 -*
import os
import sys
from setuptools import setup, find_packages


readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(version))
    print("  git push --tags")
    sys.exit()

setup(
    name='python-postmark-inbound',
    version='1.0.0',
    packages=find_packages(),
    author='José Padilla',
    author_email='jpadilla@webapplicate.com',
    description='Python wrapper for Postmark Inbound',
    long_description=long_description,
    license='MIT License',
    url='https://github.com/jpadilla/postmark-inbound-python',
    download_url='https://github.com/jpadilla/postmark-inbound-python/tarball/master',
)
