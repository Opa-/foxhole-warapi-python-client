# WarReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_enlistments** | **int** |  | [optional] 
**colonial_casualties** | **int** |  | [optional] 
**warden_casualties** | **int** |  | [optional] 
**day_of_war** | **int** |  | [optional] 

## Example

```python
from warapi_client.models.war_report import WarReport

# TODO update the JSON string below
json = "{}"
# create an instance of WarReport from a JSON string
war_report_instance = WarReport.from_json(json)
# print the JSON string representation of the object
print(WarReport.to_json())

# convert the object into a dict
war_report_dict = war_report_instance.to_dict()
# create an instance of WarReport from a dict
war_report_from_dict = WarReport.from_dict(war_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


