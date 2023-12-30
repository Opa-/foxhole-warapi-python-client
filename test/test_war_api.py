# coding: utf-8

"""
    WarAPI

    The War API allows developers to query information about the state of the current Foxhole World Conquest.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import warapi_client
from warapi_client.api.war_api import WarApi  # noqa: E501
from warapi_client.rest import ApiException


class TestWarApi(unittest.TestCase):
    """WarApi unit test stubs"""

    def setUp(self):
        self.api = WarApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_war(self):
        """Test case for get_war

        Returns data about the current state of the war.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()