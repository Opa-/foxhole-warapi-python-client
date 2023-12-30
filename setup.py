# coding: utf-8

"""
    WarAPI

    The War API allows developers to query information about the state of the current Foxhole World Conquest.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "foxhole-warapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="WarAPI",
    author_email="",
    url="",
    keywords=["Swagger", "WarAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The War API allows developers to query information about the state of the current Foxhole World Conquest.  # noqa: E501
    """
)
