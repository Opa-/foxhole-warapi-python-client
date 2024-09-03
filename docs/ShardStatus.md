# ShardStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_show_colonial_queue_warning** | **bool** |  | [optional] 
**b_show_warden_queue_warning** | **bool** |  | [optional] 
**normalized_global_population** | **float** |  | [optional] 
**server_connection_info_list** | [**List[ServerConnectionInfo]**](ServerConnectionInfo.md) |  | [optional] 
**war_id** | **str** |  | [optional] 
**squad_max_size** | **int** |  | [optional] 
**seconds_to_pre_conquest** | **int** |  | [optional] 
**b_is_pre_conquest** | **bool** |  | [optional] 
**b_is_vip_mode** | **bool** |  | [optional] 

## Example

```python
from warapi.models.shard_status import ShardStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ShardStatus from a JSON string
shard_status_instance = ShardStatus.from_json(json)
# print the JSON string representation of the object
print(ShardStatus.to_json())

# convert the object into a dict
shard_status_dict = shard_status_instance.to_dict()
# create an instance of ShardStatus from a dict
shard_status_from_dict = ShardStatus.from_dict(shard_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


