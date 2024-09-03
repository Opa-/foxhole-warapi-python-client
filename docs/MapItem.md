# MapItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | [**FactionEnum**](FactionEnum.md) |  | [optional] 
**icon_type** | **int** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**flags** | **int** |  | [optional] 
**view_direction** | **int** |  | [optional] 

## Example

```python
from warapi.models.map_item import MapItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapItem from a JSON string
map_item_instance = MapItem.from_json(json)
# print the JSON string representation of the object
print(MapItem.to_json())

# convert the object into a dict
map_item_dict = map_item_instance.to_dict()
# create an instance of MapItem from a dict
map_item_from_dict = MapItem.from_dict(map_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


