# warapi_client.MapsApi

All URIs are relative to *https://war-service-live.foxholeservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_map_dynamic**](MapsApi.md#get_map_dynamic) | **GET** /worldconquest/maps/{mapName}/dynamic/public | Dynamic map data includes map icons that could change over the lifecycle of a map. This includes static bases and static base build sites.
[**get_map_static**](MapsApi.md#get_map_static) | **GET** /worldconquest/maps/{mapName}/static | Static map data includes things that never change over the lifecycle of a map. This includes map text labels, resource nodes, and world structures.
[**get_maps**](MapsApi.md#get_maps) | **GET** /worldconquest/maps | Returns a list of the active World Conquest map names.
[**get_war_report**](MapsApi.md#get_war_report) | **GET** /worldconquest/warReport/{mapName} | Returns the number of enlistments, casualties, and other map specific information.


# **get_map_dynamic**
> Map get_map_dynamic(map_name, if_none_match=if_none_match)

Dynamic map data includes map icons that could change over the lifecycle of a map. This includes static bases and static base build sites.

<p>Team-specific data and forward bases are excluded.</p><i>This data may update every 3 seconds.</i>

### Example


```python
import warapi_client
from warapi_client.models.map import Map
from warapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://war-service-live.foxholeservices.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = warapi_client.Configuration(
    host = "https://war-service-live.foxholeservices.com/api"
)


# Enter a context with an instance of the API client
with warapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = warapi_client.MapsApi(api_client)
    map_name = 'DeadLandsHex' # str | Name of the map
    if_none_match = '10' # str | https://datatracker.ietf.org/doc/html/rfc7232 (optional)

    try:
        # Dynamic map data includes map icons that could change over the lifecycle of a map. This includes static bases and static base build sites.
        api_response = api_instance.get_map_dynamic(map_name, if_none_match=if_none_match)
        print("The response of MapsApi->get_map_dynamic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_map_dynamic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Name of the map | 
 **if_none_match** | **str**| https://datatracker.ietf.org/doc/html/rfc7232 | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * ETag -  <br>  |
**304** | Resource not modified |  * ETag -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_static**
> Map get_map_static(map_name, if_none_match=if_none_match)

Static map data includes things that never change over the lifecycle of a map. This includes map text labels, resource nodes, and world structures.

<p></p><i>You only need to request this once per map between World Conquests.</i>

### Example


```python
import warapi_client
from warapi_client.models.map import Map
from warapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://war-service-live.foxholeservices.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = warapi_client.Configuration(
    host = "https://war-service-live.foxholeservices.com/api"
)


# Enter a context with an instance of the API client
with warapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = warapi_client.MapsApi(api_client)
    map_name = 'DeadLandsHex' # str | Name of the map
    if_none_match = '10' # str | https://datatracker.ietf.org/doc/html/rfc7232 (optional)

    try:
        # Static map data includes things that never change over the lifecycle of a map. This includes map text labels, resource nodes, and world structures.
        api_response = api_instance.get_map_static(map_name, if_none_match=if_none_match)
        print("The response of MapsApi->get_map_static:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_map_static: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Name of the map | 
 **if_none_match** | **str**| https://datatracker.ietf.org/doc/html/rfc7232 | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * ETag -  <br>  |
**304** | Resource not modified |  * ETag -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maps**
> List[str] get_maps()

Returns a list of the active World Conquest map names.

<p>Note: The maps HomeRegionC and HomeRegionW are returned here, but do not have map data available in this version.</p>

### Example


```python
import warapi_client
from warapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://war-service-live.foxholeservices.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = warapi_client.Configuration(
    host = "https://war-service-live.foxholeservices.com/api"
)


# Enter a context with an instance of the API client
with warapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = warapi_client.MapsApi(api_client)

    try:
        # Returns a list of the active World Conquest map names.
        api_response = api_instance.get_maps()
        print("The response of MapsApi->get_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_maps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_war_report**
> WarReport get_war_report(map_name, if_none_match=if_none_match)

Returns the number of enlistments, casualties, and other map specific information.

<p></p><i>This data may update every 3 seconds.</i>

### Example


```python
import warapi_client
from warapi_client.models.war_report import WarReport
from warapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://war-service-live.foxholeservices.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = warapi_client.Configuration(
    host = "https://war-service-live.foxholeservices.com/api"
)


# Enter a context with an instance of the API client
with warapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = warapi_client.MapsApi(api_client)
    map_name = 'DeadLandsHex' # str | Name of the map
    if_none_match = '10' # str | https://datatracker.ietf.org/doc/html/rfc7232 (optional)

    try:
        # Returns the number of enlistments, casualties, and other map specific information.
        api_response = api_instance.get_war_report(map_name, if_none_match=if_none_match)
        print("The response of MapsApi->get_war_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_war_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Name of the map | 
 **if_none_match** | **str**| https://datatracker.ietf.org/doc/html/rfc7232 | [optional] 

### Return type

[**WarReport**](WarReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * ETag -  <br>  |
**304** | Resource not modified |  * ETag -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

