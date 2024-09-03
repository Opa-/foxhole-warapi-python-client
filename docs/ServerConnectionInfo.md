# ServerConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_map** | **str** |  | [optional] 
**steam_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**beacon_port** | **int** |  | [optional] 
**packed_war_status** | **int** |  | [optional] 
**packed_server_state** | **int** |  | [optional] 
**colonial_queue_size** | **int** |  | [optional] 
**warden_queue_size** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**server_type** | **int** |  | [optional] 
**map_id** | **int** |  | [optional] 
**open_colonial_slots** | **int** |  | [optional] 
**open_warden_slots** | **int** |  | [optional] 
**free_disk_space_in_mb** | **int** |  | [optional] 
**total_disk_space_in_mb** | **int** |  | [optional] 

## Example

```python
from warapi_client.models.server_connection_info import ServerConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConnectionInfo from a JSON string
server_connection_info_instance = ServerConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(ServerConnectionInfo.to_json())

# convert the object into a dict
server_connection_info_dict = server_connection_info_instance.to_dict()
# create an instance of ServerConnectionInfo from a dict
server_connection_info_from_dict = ServerConnectionInfo.from_dict(server_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


