# openapi_client.SecureTokenManagementApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_tokens_activations_delete**](SecureTokenManagementApi.md#secure_tokens_activations_delete) | **DELETE** /secure/tokens/activations | This API is used for deactivating merchant token securely
[**secure_tokens_details_post**](SecureTokenManagementApi.md#secure_tokens_details_post) | **POST** /secure/tokens/details | This API is used for getting details of Merchant Token by Token link.


# **secure_tokens_activations_delete**
> secure_tokens_activations_delete(x_api_key, x_app_key, x_version, origin, token_request)

This API is used for deactivating merchant token securely

### Example


```python
import openapi_client
from openapi_client.models.token_request import TokenRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uat.anddone.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uat.anddone.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecureTokenManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    token_request = openapi_client.TokenRequest() # TokenRequest | secure merchant token request

    try:
        # This API is used for deactivating merchant token securely
        api_instance.secure_tokens_activations_delete(x_api_key, x_app_key, x_version, origin, token_request)
    except Exception as e:
        print("Exception when calling SecureTokenManagementApi->secure_tokens_activations_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **token_request** | [**TokenRequest**](TokenRequest.md)| secure merchant token request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secure_tokens_details_post**
> SecureMerchantTokenShortResponse secure_tokens_details_post(x_api_key, x_app_key, x_version, origin, secure_token_link_request)

This API is used for getting details of Merchant Token by Token link.

### Example


```python
import openapi_client
from openapi_client.models.secure_merchant_token_short_response import SecureMerchantTokenShortResponse
from openapi_client.models.secure_token_link_request import SecureTokenLinkRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uat.anddone.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uat.anddone.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecureTokenManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_token_link_request = openapi_client.SecureTokenLinkRequest() # SecureTokenLinkRequest | Secure Token Link Id Request

    try:
        # This API is used for getting details of Merchant Token by Token link.
        api_response = api_instance.secure_tokens_details_post(x_api_key, x_app_key, x_version, origin, secure_token_link_request)
        print("The response of SecureTokenManagementApi->secure_tokens_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureTokenManagementApi->secure_tokens_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_token_link_request** | [**SecureTokenLinkRequest**](SecureTokenLinkRequest.md)| Secure Token Link Id Request | 

### Return type

[**SecureMerchantTokenShortResponse**](SecureMerchantTokenShortResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

