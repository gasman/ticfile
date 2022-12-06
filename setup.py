#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ticfile",
    version="0.1",
    description="A library for reading and writing TIC-80 .tic cartridge files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Matt Westcott",
    author_email="matt@west.co.tt",
    url="https://github.com/gasman/ticfile",
    py_modules=['ticfile'],
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Emulators",
    ],
    python_requires=">=3.7",
    install_requires=[],
    zip_safe=True,
)
