from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bupectomy',
    version='1.0.0',
    description='Python script which assists with the handling of McAfee .bup files',
    long_description=long_description,
    url='https://github.com/PoorBillionaire/bupectomy',
    author='Adam Witt',
    author_email='accidentalassist@gmail.com',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ],

    install_requires=['olefile'],
    keywords='DFIR Malware Forensics Incident Response IR McAfee',
    packages=find_packages(),
    scripts=['bupectomy/bupectomy.py'],
)
