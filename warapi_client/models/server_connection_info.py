# coding: utf-8

"""
    WarAPI

    The War API allows developers to query information about the state of the current Foxhole World Conquest.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServerConnectionInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_map': 'str',
        'steam_id': 'str',
        'ip_address': 'str',
        'port': 'int',
        'beacon_port': 'int',
        'packed_war_status': 'int',
        'packed_server_state': 'int',
        'colonial_queue_size': 'int',
        'warden_queue_size': 'int',
        'name': 'str',
        'version': 'str',
        'server_type': 'int',
        'map_id': 'int',
        'open_colonial_slots': 'int',
        'open_warden_slots': 'int',
        'free_disk_space_in_mb': 'int',
        'total_disk_space_in_mb': 'int'
    }

    attribute_map = {
        'current_map': 'currentMap',
        'steam_id': 'steamId',
        'ip_address': 'ipAddress',
        'port': 'port',
        'beacon_port': 'beaconPort',
        'packed_war_status': 'packedWarStatus',
        'packed_server_state': 'packedServerState',
        'colonial_queue_size': 'colonialQueueSize',
        'warden_queue_size': 'wardenQueueSize',
        'name': 'name',
        'version': 'version',
        'server_type': 'serverType',
        'map_id': 'mapId',
        'open_colonial_slots': 'openColonialSlots',
        'open_warden_slots': 'openWardenSlots',
        'free_disk_space_in_mb': 'freeDiskSpaceInMb',
        'total_disk_space_in_mb': 'totalDiskSpaceInMb'
    }

    def __init__(self, current_map=None, steam_id=None, ip_address=None, port=None, beacon_port=None, packed_war_status=None, packed_server_state=None, colonial_queue_size=None, warden_queue_size=None, name=None, version=None, server_type=None, map_id=None, open_colonial_slots=None, open_warden_slots=None, free_disk_space_in_mb=None, total_disk_space_in_mb=None):  # noqa: E501
        """ServerConnectionInfo - a model defined in Swagger"""  # noqa: E501
        self._current_map = None
        self._steam_id = None
        self._ip_address = None
        self._port = None
        self._beacon_port = None
        self._packed_war_status = None
        self._packed_server_state = None
        self._colonial_queue_size = None
        self._warden_queue_size = None
        self._name = None
        self._version = None
        self._server_type = None
        self._map_id = None
        self._open_colonial_slots = None
        self._open_warden_slots = None
        self._free_disk_space_in_mb = None
        self._total_disk_space_in_mb = None
        self.discriminator = None
        if current_map is not None:
            self.current_map = current_map
        if steam_id is not None:
            self.steam_id = steam_id
        if ip_address is not None:
            self.ip_address = ip_address
        if port is not None:
            self.port = port
        if beacon_port is not None:
            self.beacon_port = beacon_port
        if packed_war_status is not None:
            self.packed_war_status = packed_war_status
        if packed_server_state is not None:
            self.packed_server_state = packed_server_state
        if colonial_queue_size is not None:
            self.colonial_queue_size = colonial_queue_size
        if warden_queue_size is not None:
            self.warden_queue_size = warden_queue_size
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if server_type is not None:
            self.server_type = server_type
        if map_id is not None:
            self.map_id = map_id
        if open_colonial_slots is not None:
            self.open_colonial_slots = open_colonial_slots
        if open_warden_slots is not None:
            self.open_warden_slots = open_warden_slots
        if free_disk_space_in_mb is not None:
            self.free_disk_space_in_mb = free_disk_space_in_mb
        if total_disk_space_in_mb is not None:
            self.total_disk_space_in_mb = total_disk_space_in_mb

    @property
    def current_map(self):
        """Gets the current_map of this ServerConnectionInfo.  # noqa: E501


        :return: The current_map of this ServerConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._current_map

    @current_map.setter
    def current_map(self, current_map):
        """Sets the current_map of this ServerConnectionInfo.


        :param current_map: The current_map of this ServerConnectionInfo.  # noqa: E501
        :type: str
        """

        self._current_map = current_map

    @property
    def steam_id(self):
        """Gets the steam_id of this ServerConnectionInfo.  # noqa: E501


        :return: The steam_id of this ServerConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._steam_id

    @steam_id.setter
    def steam_id(self, steam_id):
        """Sets the steam_id of this ServerConnectionInfo.


        :param steam_id: The steam_id of this ServerConnectionInfo.  # noqa: E501
        :type: str
        """

        self._steam_id = steam_id

    @property
    def ip_address(self):
        """Gets the ip_address of this ServerConnectionInfo.  # noqa: E501


        :return: The ip_address of this ServerConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ServerConnectionInfo.


        :param ip_address: The ip_address of this ServerConnectionInfo.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def port(self):
        """Gets the port of this ServerConnectionInfo.  # noqa: E501


        :return: The port of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerConnectionInfo.


        :param port: The port of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def beacon_port(self):
        """Gets the beacon_port of this ServerConnectionInfo.  # noqa: E501


        :return: The beacon_port of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._beacon_port

    @beacon_port.setter
    def beacon_port(self, beacon_port):
        """Sets the beacon_port of this ServerConnectionInfo.


        :param beacon_port: The beacon_port of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._beacon_port = beacon_port

    @property
    def packed_war_status(self):
        """Gets the packed_war_status of this ServerConnectionInfo.  # noqa: E501


        :return: The packed_war_status of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._packed_war_status

    @packed_war_status.setter
    def packed_war_status(self, packed_war_status):
        """Sets the packed_war_status of this ServerConnectionInfo.


        :param packed_war_status: The packed_war_status of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._packed_war_status = packed_war_status

    @property
    def packed_server_state(self):
        """Gets the packed_server_state of this ServerConnectionInfo.  # noqa: E501


        :return: The packed_server_state of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._packed_server_state

    @packed_server_state.setter
    def packed_server_state(self, packed_server_state):
        """Sets the packed_server_state of this ServerConnectionInfo.


        :param packed_server_state: The packed_server_state of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._packed_server_state = packed_server_state

    @property
    def colonial_queue_size(self):
        """Gets the colonial_queue_size of this ServerConnectionInfo.  # noqa: E501


        :return: The colonial_queue_size of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._colonial_queue_size

    @colonial_queue_size.setter
    def colonial_queue_size(self, colonial_queue_size):
        """Sets the colonial_queue_size of this ServerConnectionInfo.


        :param colonial_queue_size: The colonial_queue_size of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._colonial_queue_size = colonial_queue_size

    @property
    def warden_queue_size(self):
        """Gets the warden_queue_size of this ServerConnectionInfo.  # noqa: E501


        :return: The warden_queue_size of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._warden_queue_size

    @warden_queue_size.setter
    def warden_queue_size(self, warden_queue_size):
        """Sets the warden_queue_size of this ServerConnectionInfo.


        :param warden_queue_size: The warden_queue_size of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._warden_queue_size = warden_queue_size

    @property
    def name(self):
        """Gets the name of this ServerConnectionInfo.  # noqa: E501


        :return: The name of this ServerConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerConnectionInfo.


        :param name: The name of this ServerConnectionInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this ServerConnectionInfo.  # noqa: E501


        :return: The version of this ServerConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ServerConnectionInfo.


        :param version: The version of this ServerConnectionInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def server_type(self):
        """Gets the server_type of this ServerConnectionInfo.  # noqa: E501


        :return: The server_type of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this ServerConnectionInfo.


        :param server_type: The server_type of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._server_type = server_type

    @property
    def map_id(self):
        """Gets the map_id of this ServerConnectionInfo.  # noqa: E501


        :return: The map_id of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this ServerConnectionInfo.


        :param map_id: The map_id of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._map_id = map_id

    @property
    def open_colonial_slots(self):
        """Gets the open_colonial_slots of this ServerConnectionInfo.  # noqa: E501


        :return: The open_colonial_slots of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._open_colonial_slots

    @open_colonial_slots.setter
    def open_colonial_slots(self, open_colonial_slots):
        """Sets the open_colonial_slots of this ServerConnectionInfo.


        :param open_colonial_slots: The open_colonial_slots of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._open_colonial_slots = open_colonial_slots

    @property
    def open_warden_slots(self):
        """Gets the open_warden_slots of this ServerConnectionInfo.  # noqa: E501


        :return: The open_warden_slots of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._open_warden_slots

    @open_warden_slots.setter
    def open_warden_slots(self, open_warden_slots):
        """Sets the open_warden_slots of this ServerConnectionInfo.


        :param open_warden_slots: The open_warden_slots of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._open_warden_slots = open_warden_slots

    @property
    def free_disk_space_in_mb(self):
        """Gets the free_disk_space_in_mb of this ServerConnectionInfo.  # noqa: E501


        :return: The free_disk_space_in_mb of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._free_disk_space_in_mb

    @free_disk_space_in_mb.setter
    def free_disk_space_in_mb(self, free_disk_space_in_mb):
        """Sets the free_disk_space_in_mb of this ServerConnectionInfo.


        :param free_disk_space_in_mb: The free_disk_space_in_mb of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._free_disk_space_in_mb = free_disk_space_in_mb

    @property
    def total_disk_space_in_mb(self):
        """Gets the total_disk_space_in_mb of this ServerConnectionInfo.  # noqa: E501


        :return: The total_disk_space_in_mb of this ServerConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_disk_space_in_mb

    @total_disk_space_in_mb.setter
    def total_disk_space_in_mb(self, total_disk_space_in_mb):
        """Sets the total_disk_space_in_mb of this ServerConnectionInfo.


        :param total_disk_space_in_mb: The total_disk_space_in_mb of this ServerConnectionInfo.  # noqa: E501
        :type: int
        """

        self._total_disk_space_in_mb = total_disk_space_in_mb

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ServerConnectionInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
