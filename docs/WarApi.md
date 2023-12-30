# warapi_client.WarApi

All URIs are relative to *https://war-service-live.foxholeservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_war**](WarApi.md#get_war) | **GET** /worldconquest/war | Returns data about the current state of the war.

# **get_war**
> War get_war()

Returns data about the current state of the war.

<p>The number of required victory towns that's returned by this endpoint represents a static configuration value and does not take any scorched victory towns into account. This means that if you wish to determine how many victory towns are required to win the war, you must reduce it by one for each scorched victory town. A scorched victory town is any map item that has both the IsVictoryBase and IsScorched flags set. See the Map Data section for more details.</p> <i>This data may update every 60 seconds.</i>

### Example
```python
from __future__ import print_function
import time
import warapi_client
from warapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = warapi_client.WarApi()

try:
    # Returns data about the current state of the war.
    api_response = api_instance.get_war()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarApi->get_war: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**War**](War.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

