# War


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**war_id** | **str** |  | [optional] 
**war_number** | **int** |  | [optional] 
**winner** | [**FactionEnum**](FactionEnum.md) |  | [optional] 
**conquest_start_time** | **int** |  | [optional] 
**conquest_end_time** | **int** |  | [optional] 
**resistance_start_time** | **int** |  | [optional] 
**required_victory_towns** | **int** |  | [optional] 

## Example

```python
from warapi.models.war import War

# TODO update the JSON string below
json = "{}"
# create an instance of War from a JSON string
war_instance = War.from_json(json)
# print the JSON string representation of the object
print(War.to_json())

# convert the object into a dict
war_dict = war_instance.to_dict()
# create an instance of War from a dict
war_from_dict = War.from_dict(war_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


