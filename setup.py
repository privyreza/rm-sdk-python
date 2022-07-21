#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="rm_sdk_python",
    version="1.0.4",
    description="The Official Resellme Python SDK .",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Beven Nyamande aka 0xbeven",
    author_email="bevenfx@gmail.com",
    url="https://github.com/bevennyamande/rm-sdk-python/",
    project_urls={
        "Homepage" : "https://github.com/bevennyamande/rm-sdk-python/",
        "Bug Tracker": "https://github.com/bevennyamande/rm-sdk-python/issues",
    },
    install_requires=[
        "requests",
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
