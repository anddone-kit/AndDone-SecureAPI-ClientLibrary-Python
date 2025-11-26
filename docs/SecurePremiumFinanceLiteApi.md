# openapi_client.SecurePremiumFinanceLiteApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_epflite_quotes_generate_post**](SecurePremiumFinanceLiteApi.md#secure_epflite_quotes_generate_post) | **POST** /secure/epflite/quotes/generate | This API is used to generate the quote from the provider.
[**secure_epflite_quotes_link_post**](SecurePremiumFinanceLiteApi.md#secure_epflite_quotes_link_post) | **POST** /secure/epflite/quotes/link | This API will return quotes created againsts a payment link.
[**secure_epflite_quotes_paymentlinks_post**](SecurePremiumFinanceLiteApi.md#secure_epflite_quotes_paymentlinks_post) | **POST** /secure/epflite/quotes/paymentlinks | This API is used to create Payment Links


# **secure_epflite_quotes_generate_post**
> PFLiteGenerateQuoteResponse secure_epflite_quotes_generate_post(x_api_key, x_app_key, x_version, origin, pf_lite_secure_quote_request=pf_lite_secure_quote_request)

This API is used to generate the quote from the provider.

### Example


```python
import openapi_client
from openapi_client.models.pf_lite_generate_quote_response import PFLiteGenerateQuoteResponse
from openapi_client.models.pf_lite_secure_quote_request import PFLiteSecureQuoteRequest
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
    api_instance = openapi_client.SecurePremiumFinanceLiteApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    pf_lite_secure_quote_request = openapi_client.PFLiteSecureQuoteRequest() # PFLiteSecureQuoteRequest | PFLite Quote Secure Request details (optional)

    try:
        # This API is used to generate the quote from the provider.
        api_response = api_instance.secure_epflite_quotes_generate_post(x_api_key, x_app_key, x_version, origin, pf_lite_secure_quote_request=pf_lite_secure_quote_request)
        print("The response of SecurePremiumFinanceLiteApi->secure_epflite_quotes_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePremiumFinanceLiteApi->secure_epflite_quotes_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **pf_lite_secure_quote_request** | [**PFLiteSecureQuoteRequest**](PFLiteSecureQuoteRequest.md)| PFLite Quote Secure Request details | [optional] 

### Return type

[**PFLiteGenerateQuoteResponse**](PFLiteGenerateQuoteResponse.md)

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

# **secure_epflite_quotes_link_post**
> List[PFLiteQuoteByPaymentLinkResponse] secure_epflite_quotes_link_post(x_api_key, x_app_key, x_version, origin, pf_lite_get_quote_request=pf_lite_get_quote_request)

This API will return quotes created againsts a payment link.

### Example


```python
import openapi_client
from openapi_client.models.pf_lite_get_quote_request import PFLiteGetQuoteRequest
from openapi_client.models.pf_lite_quote_by_payment_link_response import PFLiteQuoteByPaymentLinkResponse
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
    api_instance = openapi_client.SecurePremiumFinanceLiteApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    pf_lite_get_quote_request = openapi_client.PFLiteGetQuoteRequest() # PFLiteGetQuoteRequest | Signature Request details (optional)

    try:
        # This API will return quotes created againsts a payment link.
        api_response = api_instance.secure_epflite_quotes_link_post(x_api_key, x_app_key, x_version, origin, pf_lite_get_quote_request=pf_lite_get_quote_request)
        print("The response of SecurePremiumFinanceLiteApi->secure_epflite_quotes_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePremiumFinanceLiteApi->secure_epflite_quotes_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **pf_lite_get_quote_request** | [**PFLiteGetQuoteRequest**](PFLiteGetQuoteRequest.md)| Signature Request details | [optional] 

### Return type

[**List[PFLiteQuoteByPaymentLinkResponse]**](PFLiteQuoteByPaymentLinkResponse.md)

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

# **secure_epflite_quotes_paymentlinks_post**
> PaymentLinkResponse secure_epflite_quotes_paymentlinks_post(x_api_key, x_app_key, x_version, origin, pf_lite_payment_link_request)

This API is used to create Payment Links

### Example


```python
import openapi_client
from openapi_client.models.pf_lite_payment_link_request import PFLitePaymentLinkRequest
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
    api_instance = openapi_client.SecurePremiumFinanceLiteApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    pf_lite_payment_link_request = openapi_client.PFLitePaymentLinkRequest() # PFLitePaymentLinkRequest | Payment Link Request

    try:
        # This API is used to create Payment Links
        api_response = api_instance.secure_epflite_quotes_paymentlinks_post(x_api_key, x_app_key, x_version, origin, pf_lite_payment_link_request)
        print("The response of SecurePremiumFinanceLiteApi->secure_epflite_quotes_paymentlinks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePremiumFinanceLiteApi->secure_epflite_quotes_paymentlinks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **pf_lite_payment_link_request** | [**PFLitePaymentLinkRequest**](PFLitePaymentLinkRequest.md)| Payment Link Request | 

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

