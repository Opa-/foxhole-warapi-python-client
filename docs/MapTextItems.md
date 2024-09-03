# MapTextItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**map_marker_type** | **str** |  | [optional] 

## Example

```python
from warapi_client.models.map_text_items import MapTextItems

# TODO update the JSON string below
json = "{}"
# create an instance of MapTextItems from a JSON string
map_text_items_instance = MapTextItems.from_json(json)
# print the JSON string representation of the object
print(MapTextItems.to_json())

# convert the object into a dict
map_text_items_dict = map_text_items_instance.to_dict()
# create an instance of MapTextItems from a dict
map_text_items_from_dict = MapTextItems.from_dict(map_text_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


