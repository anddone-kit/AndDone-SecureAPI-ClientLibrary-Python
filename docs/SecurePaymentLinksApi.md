# openapi_client.SecurePaymentLinksApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_paymentlinks_details_post**](SecurePaymentLinksApi.md#secure_paymentlinks_details_post) | **POST** /secure/paymentlinks/details | This API is used for getting Payment Links by PaymentLink ID
[**secure_paymentlinks_expirations_post**](SecurePaymentLinksApi.md#secure_paymentlinks_expirations_post) | **POST** /secure/paymentlinks/expirations | This API is used for to set expired payment link
[**secure_paymentlinks_id_put**](SecurePaymentLinksApi.md#secure_paymentlinks_id_put) | **PUT** /secure/paymentlinks/{id} | This API is used to update Payment Links
[**secure_paymentlinks_post**](SecurePaymentLinksApi.md#secure_paymentlinks_post) | **POST** /secure/paymentlinks | This API is used to create Payment Links


# **secure_paymentlinks_details_post**
> PaymentLinkResponse secure_paymentlinks_details_post(x_api_key, x_app_key, x_version, origin, secure_payment_link_request)

This API is used for getting Payment Links by PaymentLink ID

### Example


```python
import openapi_client
from openapi_client.models.payment_link_response import PaymentLinkResponse
from openapi_client.models.secure_payment_link_request import SecurePaymentLinkRequest
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
    api_instance = openapi_client.SecurePaymentLinksApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_payment_link_request = openapi_client.SecurePaymentLinkRequest() # SecurePaymentLinkRequest | Secure Payment Link Request

    try:
        # This API is used for getting Payment Links by PaymentLink ID
        api_response = api_instance.secure_paymentlinks_details_post(x_api_key, x_app_key, x_version, origin, secure_payment_link_request)
        print("The response of SecurePaymentLinksApi->secure_paymentlinks_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentLinksApi->secure_paymentlinks_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_payment_link_request** | [**SecurePaymentLinkRequest**](SecurePaymentLinkRequest.md)| Secure Payment Link Request | 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secure_paymentlinks_expirations_post**
> PaymentLinkExpiresResponse secure_paymentlinks_expirations_post(x_api_key, x_app_key, x_version, origin, secure_payment_link_request=secure_payment_link_request)

This API is used for to set expired payment link

### Example


```python
import openapi_client
from openapi_client.models.payment_link_expires_response import PaymentLinkExpiresResponse
from openapi_client.models.secure_payment_link_request import SecurePaymentLinkRequest
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
    api_instance = openapi_client.SecurePaymentLinksApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_payment_link_request = openapi_client.SecurePaymentLinkRequest() # SecurePaymentLinkRequest | Secure Payment Link Request (optional)

    try:
        # This API is used for to set expired payment link
        api_response = api_instance.secure_paymentlinks_expirations_post(x_api_key, x_app_key, x_version, origin, secure_payment_link_request=secure_payment_link_request)
        print("The response of SecurePaymentLinksApi->secure_paymentlinks_expirations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentLinksApi->secure_paymentlinks_expirations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_payment_link_request** | [**SecurePaymentLinkRequest**](SecurePaymentLinkRequest.md)| Secure Payment Link Request | [optional] 

### Return type

[**PaymentLinkExpiresResponse**](PaymentLinkExpiresResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secure_paymentlinks_id_put**
> PaymentLinkResponse secure_paymentlinks_id_put(x_api_key, x_app_key, x_version, origin, id, secure_update_payment_link_request)

This API is used to update Payment Links

### Example


```python
import openapi_client
from openapi_client.models.payment_link_response import PaymentLinkResponse
from openapi_client.models.secure_update_payment_link_request import SecureUpdatePaymentLinkRequest
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
    api_instance = openapi_client.SecurePaymentLinksApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    id = 'id_example' # str | PaymentLink identifier
    secure_update_payment_link_request = openapi_client.SecureUpdatePaymentLinkRequest() # SecureUpdatePaymentLinkRequest | Payment Link Request

    try:
        # This API is used to update Payment Links
        api_response = api_instance.secure_paymentlinks_id_put(x_api_key, x_app_key, x_version, origin, id, secure_update_payment_link_request)
        print("The response of SecurePaymentLinksApi->secure_paymentlinks_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentLinksApi->secure_paymentlinks_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **id** | **str**| PaymentLink identifier | 
 **secure_update_payment_link_request** | [**SecureUpdatePaymentLinkRequest**](SecureUpdatePaymentLinkRequest.md)| Payment Link Request | 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

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

# **secure_paymentlinks_post**
> PaymentLinkResponse secure_paymentlinks_post(x_api_key, x_app_key, x_version, origin, payment_link_request)

This API is used to create Payment Links

### Example


```python
import openapi_client
from openapi_client.models.payment_link_request import PaymentLinkRequest
from openapi_client.models.payment_link_response import PaymentLinkResponse
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
    api_instance = openapi_client.SecurePaymentLinksApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    payment_link_request = openapi_client.PaymentLinkRequest() # PaymentLinkRequest | Payment Link Request

    try:
        # This API is used to create Payment Links
        api_response = api_instance.secure_paymentlinks_post(x_api_key, x_app_key, x_version, origin, payment_link_request)
        print("The response of SecurePaymentLinksApi->secure_paymentlinks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentLinksApi->secure_paymentlinks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **payment_link_request** | [**PaymentLinkRequest**](PaymentLinkRequest.md)| Payment Link Request | 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

