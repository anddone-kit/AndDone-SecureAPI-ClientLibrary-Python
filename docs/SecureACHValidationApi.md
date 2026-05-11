# openapi_client.SecureACHValidationApi

All URIs are relative to *https://api.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utilityapi_secure_verifybankaccounts_post**](SecureACHValidationApi.md#utilityapi_secure_verifybankaccounts_post) | **POST** /utilityapi/secure/verifybankaccounts | This API verifies bank account using secure ACH validation


# **utilityapi_secure_verifybankaccounts_post**
> VerifyBankAccountResponse utilityapi_secure_verifybankaccounts_post(x_api_key, x_app_key, x_version, origin, secure_verify_bank_account_request_dto)

This API verifies bank account using secure ACH validation

### Example


```python
import openapi_client
from openapi_client.models.secure_verify_bank_account_request_dto import SecureVerifyBankAccountRequestDTO
from openapi_client.models.verify_bank_account_response import VerifyBankAccountResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.anddone.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.anddone.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecureACHValidationApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 3.4 # float | x-version
    origin = 'origin_example' # str | origin
    secure_verify_bank_account_request_dto = openapi_client.SecureVerifyBankAccountRequestDTO() # SecureVerifyBankAccountRequestDTO | SecureVerifyBankAccountRequestDTO

    try:
        # This API verifies bank account using secure ACH validation
        api_response = api_instance.utilityapi_secure_verifybankaccounts_post(x_api_key, x_app_key, x_version, origin, secure_verify_bank_account_request_dto)
        print("The response of SecureACHValidationApi->utilityapi_secure_verifybankaccounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureACHValidationApi->utilityapi_secure_verifybankaccounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **float**| x-version | 
 **origin** | **str**| origin | 
 **secure_verify_bank_account_request_dto** | [**SecureVerifyBankAccountRequestDTO**](SecureVerifyBankAccountRequestDTO.md)| SecureVerifyBankAccountRequestDTO | 

### Return type

[**VerifyBankAccountResponse**](VerifyBankAccountResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

