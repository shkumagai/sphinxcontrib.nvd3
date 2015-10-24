# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


version = "0.1.4"
long_description = "\n".join([
    open(os.path.join("README.rst")).read(),
    open(os.path.join("AUTHORS.rst")).read(),
    open(os.path.join("CHANGES.rst")).read(),
])

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Framework :: Sphinx",
    "Framework :: Sphinx :: Extension",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Text Processing :: Markup",
    "Topic :: Utilities",
]

setup(
    name="sphinxcontrib.nvd3",
    version=version,
    description="Sphinx chart extension using NVD3.js.",
    long_description=long_description,
    classifiers=classifiers,
    keywords=["sphinx", "d3", "visualization", "chart"],
    author="Shoji KUMAGAI",
    author_email="take.this.2.your.grave at gmail.com",
    url="https://github.com/shkumagai/sphinxcontrib.nvd3",
    license="Apache Software License",
    namespace_packages=["sphinxcontrib"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "setuptools",
        "docutils",
        "sphinx",
        "python-nvd3",
    ],
    entry_points="""
        [sphinx_directives]
        setup = sphinxcontrib.nvd3:setup
    """,
    zip_safe=False,
)
