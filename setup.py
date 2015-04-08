# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


version = "0.1.0"
long_description = "\n".join([
    open(os.path.join("src", "README.txt")).read(),
    open(os.path.join("src", "AUTHOR.txt")).read(),
    open(os.path.join("src", "HISTORY.txt")).read(),
])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
    name="sphinxcontrib.nvd3",
    version=version,
    description="A D3.js extension for Sphinx Documentation system",
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
