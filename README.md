# foxhole-warapi-client
The War API allows developers to query information about the state of the current Foxhole World Conquest.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.8.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Opa-/foxhole-warapi-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Opa-/foxhole-warapi-python-client.git`)

Then import the package:
```python
import warapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import warapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import warapi
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
    except ApiException as e:
        print("Exception when calling ExternalApi->get_shard_status: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://war-service-live.foxholeservices.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExternalApi* | [**get_shard_status**](docs/ExternalApi.md#get_shard_status) | **GET** /external/shardStatus | Hidden endpoint returning information about each server.
*MapsApi* | [**get_map_dynamic**](docs/MapsApi.md#get_map_dynamic) | **GET** /worldconquest/maps/{mapName}/dynamic/public | Dynamic map data includes map icons that could change over the lifecycle of a map. This includes static bases and static base build sites.
*MapsApi* | [**get_map_static**](docs/MapsApi.md#get_map_static) | **GET** /worldconquest/maps/{mapName}/static | Static map data includes things that never change over the lifecycle of a map. This includes map text labels, resource nodes, and world structures.
*MapsApi* | [**get_maps**](docs/MapsApi.md#get_maps) | **GET** /worldconquest/maps | Returns a list of the active World Conquest map names.
*MapsApi* | [**get_war_report**](docs/MapsApi.md#get_war_report) | **GET** /worldconquest/warReport/{mapName} | Returns the number of enlistments, casualties, and other map specific information.
*WarApi* | [**get_war**](docs/WarApi.md#get_war) | **GET** /worldconquest/war | Returns data about the current state of the war.


## Documentation For Models

 - [FactionEnum](docs/FactionEnum.md)
 - [Map](docs/Map.md)
 - [MapItem](docs/MapItem.md)
 - [MapTextItems](docs/MapTextItems.md)
 - [ServerConnectionInfo](docs/ServerConnectionInfo.md)
 - [ShardStatus](docs/ShardStatus.md)
 - [War](docs/War.md)
 - [WarReport](docs/WarReport.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




