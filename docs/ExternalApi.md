# warapi_client.ExternalApi

All URIs are relative to *https://war-service-live.foxholeservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shard_status**](ExternalApi.md#get_shard_status) | **GET** /external/shardStatus | Hidden endpoint returning information about each server.

# **get_shard_status**
> ShardStatus get_shard_status()

Hidden endpoint returning information about each server.

### Example
```python
from __future__ import print_function
import time
import warapi_client
from warapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = warapi_client.ExternalApi()

try:
    # Hidden endpoint returning information about each server.
    api_response = api_instance.get_shard_status()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

