# openapi_client.SecureAutopayEnrollmentApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_autopayenrollment_post**](SecureAutopayEnrollmentApi.md#secure_autopayenrollment_post) | **POST** /secure/autopayenrollment | This API is used for Autopay Enrollment.


# **secure_autopayenrollment_post**
> AutoPayEnrollmentResponse secure_autopayenrollment_post(x_api_key, x_app_key, x_version, origin, auto_pay_enrollment_request)

This API is used for Autopay Enrollment.

### Example


```python
import openapi_client
from openapi_client.models.auto_pay_enrollment_request import AutoPayEnrollmentRequest
from openapi_client.models.auto_pay_enrollment_response import AutoPayEnrollmentResponse
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
    api_instance = openapi_client.SecureAutopayEnrollmentApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    auto_pay_enrollment_request = openapi_client.AutoPayEnrollmentRequest() # AutoPayEnrollmentRequest | Autopay Enrollment Detail

    try:
        # This API is used for Autopay Enrollment.
        api_response = api_instance.secure_autopayenrollment_post(x_api_key, x_app_key, x_version, origin, auto_pay_enrollment_request)
        print("The response of SecureAutopayEnrollmentApi->secure_autopayenrollment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureAutopayEnrollmentApi->secure_autopayenrollment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **auto_pay_enrollment_request** | [**AutoPayEnrollmentRequest**](AutoPayEnrollmentRequest.md)| Autopay Enrollment Detail | 

### Return type

[**AutoPayEnrollmentResponse**](AutoPayEnrollmentResponse.md)

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

