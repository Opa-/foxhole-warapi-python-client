# coding: utf-8

"""
    WarAPI

    The War API allows developers to query information about the state of the current Foxhole World Conquest.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from warapi_client.models.server_connection_info import ServerConnectionInfo

class TestServerConnectionInfo(unittest.TestCase):
    """ServerConnectionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerConnectionInfo:
        """Test ServerConnectionInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerConnectionInfo`
        """
        model = ServerConnectionInfo()
        if include_optional:
            return ServerConnectionInfo(
                current_map = 'DeadLandsHex',
                steam_id = '90179095218202645',
                ip_address = '',
                port = 7777,
                beacon_port = 15000,
                packed_war_status = 864715317813116800,
                packed_server_state = 8914044,
                colonial_queue_size = 0,
                warden_queue_size = 0,
                name = 'DeadLands-5',
                version = '1.55.2.2',
                server_type = 1,
                map_id = 3,
                open_colonial_slots = 0,
                open_warden_slots = 0,
                free_disk_space_in_mb = 1277137,
                total_disk_space_in_mb = 1831090
            )
        else:
            return ServerConnectionInfo(
        )
        """

    def testServerConnectionInfo(self):
        """Test ServerConnectionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
