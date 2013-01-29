# -*- coding: utf-8 -*

import os
from setuptools import setup, find_packages

readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()

setup(
    name='python-postmark-inbound',
    version='0.1',
    packages=find_packages(),
    author='José Padilla',
    author_email='jpadilla@webapplicate.com',
    description='Python wrapper for Postmark Inbound',
    long_description=long_description,
    license='MIT License',
    url='https://github.com/jpadilla/postmark-inbound-python',
    download_url='https://github.com/jpadilla/postmark-inbound-python/tarball/master',
)
