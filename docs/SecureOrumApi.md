# openapi_client.SecureOrumApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_bankaccounts_details_post**](SecureOrumApi.md#secure_bankaccounts_details_post) | **POST** /secure/bankaccounts/details | This API will request for verified bank account.
[**secure_bankaccounts_verify_post**](SecureOrumApi.md#secure_bankaccounts_verify_post) | **POST** /secure/bankaccounts/verify | This API will request for account verification.


# **secure_bankaccounts_details_post**
> VerifyBankAccountResponse secure_bankaccounts_details_post(x_api_key, x_app_key, x_version, origin, id=id, type=type, verification_entity_request=verification_entity_request)

This API will request for verified bank account.

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.verification_entity_request import VerificationEntityRequest
from openapi_client.models.verify_bank_account_response import VerifyBankAccountResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uat.anddone.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uat.anddone.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Configure API key authorization: x-app-key
configuration.api_key['x-app-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-app-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecureOrumApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    id = 'id_example' # str | The Bank Account Entity Id (optional)
    type = 'type_example' # str | Set Type (optional)
    verification_entity_request = openapi_client.VerificationEntityRequest() # VerificationEntityRequest | Verification Entity (optional)

    try:
        # This API will request for verified bank account.
        api_response = api_instance.secure_bankaccounts_details_post(x_api_key, x_app_key, x_version, origin, id=id, type=type, verification_entity_request=verification_entity_request)
        print("The response of SecureOrumApi->secure_bankaccounts_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureOrumApi->secure_bankaccounts_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **id** | **str**| The Bank Account Entity Id | [optional] 
 **type** | **str**| Set Type | [optional] 
 **verification_entity_request** | [**VerificationEntityRequest**](VerificationEntityRequest.md)| Verification Entity | [optional] 

### Return type

[**VerifyBankAccountResponse**](VerifyBankAccountResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

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

# **secure_bankaccounts_verify_post**
> VerifyBankAccountResponse secure_bankaccounts_verify_post(x_api_key, x_app_key, x_version, origin, verify_bank_account_request=verify_bank_account_request)

This API will request for account verification.

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.verify_bank_account_request import VerifyBankAccountRequest
from openapi_client.models.verify_bank_account_response import VerifyBankAccountResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uat.anddone.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uat.anddone.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Configure API key authorization: x-app-key
configuration.api_key['x-app-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-app-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecureOrumApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    verify_bank_account_request = openapi_client.VerifyBankAccountRequest() # VerifyBankAccountRequest | Bank Accout detals (optional)

    try:
        # This API will request for account verification.
        api_response = api_instance.secure_bankaccounts_verify_post(x_api_key, x_app_key, x_version, origin, verify_bank_account_request=verify_bank_account_request)
        print("The response of SecureOrumApi->secure_bankaccounts_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureOrumApi->secure_bankaccounts_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **verify_bank_account_request** | [**VerifyBankAccountRequest**](VerifyBankAccountRequest.md)| Bank Accout detals | [optional] 

### Return type

[**VerifyBankAccountResponse**](VerifyBankAccountResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

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

