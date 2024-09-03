# warapi.ExternalApi

All URIs are relative to *https://war-service-live.foxholeservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shard_status**](ExternalApi.md#get_shard_status) | **GET** /external/shardStatus | Hidden endpoint returning information about each server.


# **get_shard_status**
> ShardStatus get_shard_status()

Hidden endpoint returning information about each server.

### Example


```python
import warapi
from warapi.models.shard_status import ShardStatus
from warapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://war-service-live.foxholeservices.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = warapi.Configuration(
    host = "https://war-service-live.foxholeservices.com/api"
)


# Enter a context with an instance of the API client
with warapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = warapi.ExternalApi(api_client)

    try:
        # Hidden endpoint returning information about each server.
        api_response = api_instance.get_shard_status()
        print("The response of ExternalApi->get_shard_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalApi->get_shard_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShardStatus**](ShardStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

