#!/usr/bin/env python

from setuptools import setup

setup(
    name="resellme",
    version="1.0.0",
    description="A minimalist python wrapper for the Resellme .",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Beven Nyamande",
    author_email="bevenfx@gmail.com",
    url="https://github.com/bevennyamande/Resellme-Python-SDK",
    py_modules=["resellme"],
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python ",
        "Programming Language :: Python :: 3.4 ",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
)
