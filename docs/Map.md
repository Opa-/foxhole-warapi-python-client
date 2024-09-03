# Map


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **int** |  | [optional] 
**scorched_victory_towns** | **int** |  | [optional] 
**map_items** | [**List[MapItem]**](MapItem.md) |  | [optional] 
**map_items_c** | [**List[MapItem]**](MapItem.md) |  | [optional] 
**map_items_w** | [**List[MapItem]**](MapItem.md) |  | [optional] 
**map_text_items** | [**List[MapTextItems]**](MapTextItems.md) |  | [optional] 
**last_updated** | **int** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from warapi_client.models.map import Map

# TODO update the JSON string below
json = "{}"
# create an instance of Map from a JSON string
map_instance = Map.from_json(json)
# print the JSON string representation of the object
print(Map.to_json())

# convert the object into a dict
map_dict = map_instance.to_dict()
# create an instance of Map from a dict
map_from_dict = Map.from_dict(map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


