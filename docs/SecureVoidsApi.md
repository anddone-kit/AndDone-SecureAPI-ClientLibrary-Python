# openapi_client.SecureVoidsApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_cancellations_post**](SecureVoidsApi.md#secure_cancellations_post) | **POST** /secure/cancellations | This API cancel a transaction.


# **secure_cancellations_post**
> SecureCancelledTransactionResponse secure_cancellations_post(x_api_key, x_app_key, x_version, origin, secure_transaction_cancel_request)

This API cancel a transaction.

### Example


```python
import openapi_client
from openapi_client.models.secure_cancelled_transaction_response import SecureCancelledTransactionResponse
from openapi_client.models.secure_transaction_cancel_request import SecureTransactionCancelRequest
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
    api_instance = openapi_client.SecureVoidsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_transaction_cancel_request = openapi_client.SecureTransactionCancelRequest() # SecureTransactionCancelRequest | Cancel Detail

    try:
        # This API cancel a transaction.
        api_response = api_instance.secure_cancellations_post(x_api_key, x_app_key, x_version, origin, secure_transaction_cancel_request)
        print("The response of SecureVoidsApi->secure_cancellations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureVoidsApi->secure_cancellations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_transaction_cancel_request** | [**SecureTransactionCancelRequest**](SecureTransactionCancelRequest.md)| Cancel Detail | 

### Return type

[**SecureCancelledTransactionResponse**](SecureCancelledTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

