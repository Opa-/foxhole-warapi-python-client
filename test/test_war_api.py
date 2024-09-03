# coding: utf-8

"""
    WarAPI

    The War API allows developers to query information about the state of the current Foxhole World Conquest.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from warapi_client.api.war_api import WarApi


class TestWarApi(unittest.TestCase):
    """WarApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WarApi()

    def tearDown(self) -> None:
        pass

    def test_get_war(self) -> None:
        """Test case for get_war

        Returns data about the current state of the war.
        """
        pass


if __name__ == '__main__':
    unittest.main()
