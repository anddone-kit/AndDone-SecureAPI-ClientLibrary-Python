# openapi_client.SecureOutboundPaymentsApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendorapi_secure_outbound_payments_timelines_post**](SecureOutboundPaymentsApi.md#vendorapi_secure_outbound_payments_timelines_post) | **POST** /vendorapi/secure/outboundPayments/timelines | This API gets outbound payment timelines
[**vendorapi_secure_outboundpayments_cancel_post**](SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_cancel_post) | **POST** /vendorapi/secure/outboundpayments/cancel | This API cancel outbound payment request
[**vendorapi_secure_outboundpayments_detail_post**](SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_detail_post) | **POST** /vendorapi/secure/outboundpayments/detail | This API fetch outbound payment by paymentId
[**vendorapi_secure_outboundpayments_post**](SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_post) | **POST** /vendorapi/secure/outboundpayments | This API creates outbound payment request
[**vendorapi_secure_outboundpayments_search_post**](SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_search_post) | **POST** /vendorapi/secure/outboundpayments/search | This API gets all outbound payment


# **vendorapi_secure_outbound_payments_timelines_post**
> List[OutboundPaymentTimelineResponseDTOInner] vendorapi_secure_outbound_payments_timelines_post(x_api_key, x_app_key, x_version, origin, payment_time_line_request_dto)

This API gets outbound payment timelines

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.outbound_payment_timeline_response_dto_inner import OutboundPaymentTimelineResponseDTOInner
from openapi_client.models.payment_time_line_request_dto import PaymentTimeLineRequestDto
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
    api_instance = openapi_client.SecureOutboundPaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    payment_time_line_request_dto = openapi_client.PaymentTimeLineRequestDto() # PaymentTimeLineRequestDto | PaymentTimeLineRequestDto

    try:
        # This API gets outbound payment timelines
        api_response = api_instance.vendorapi_secure_outbound_payments_timelines_post(x_api_key, x_app_key, x_version, origin, payment_time_line_request_dto)
        print("The response of SecureOutboundPaymentsApi->vendorapi_secure_outbound_payments_timelines_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureOutboundPaymentsApi->vendorapi_secure_outbound_payments_timelines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **payment_time_line_request_dto** | [**PaymentTimeLineRequestDto**](PaymentTimeLineRequestDto.md)| PaymentTimeLineRequestDto | 

### Return type

[**List[OutboundPaymentTimelineResponseDTOInner]**](OutboundPaymentTimelineResponseDTOInner.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OutboundPaymentTimelineResponseDTO |  -  |
**400** | Bad request or validation error |  -  |
**404** | Merchant not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_outboundpayments_cancel_post**
> vendorapi_secure_outboundpayments_cancel_post(x_api_key, x_app_key, x_version, origin, cancel_payment_request_dto)

This API cancel outbound payment request

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.cancel_payment_request_dto import CancelPaymentRequestDTO
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
    api_instance = openapi_client.SecureOutboundPaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    cancel_payment_request_dto = openapi_client.CancelPaymentRequestDTO() # CancelPaymentRequestDTO | CancelPaymentRequestDTO

    try:
        # This API cancel outbound payment request
        api_instance.vendorapi_secure_outboundpayments_cancel_post(x_api_key, x_app_key, x_version, origin, cancel_payment_request_dto)
    except Exception as e:
        print("Exception when calling SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **cancel_payment_request_dto** | [**CancelPaymentRequestDTO**](CancelPaymentRequestDTO.md)| CancelPaymentRequestDTO | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_outboundpayments_detail_post**
> PaymentDetailResponseDTO vendorapi_secure_outboundpayments_detail_post(x_api_key, x_app_key, x_version, origin, payment_request_detail_dto)

This API fetch outbound payment by paymentId

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.payment_detail_response_dto import PaymentDetailResponseDTO
from openapi_client.models.payment_request_detail_dto import PaymentRequestDetailDTO
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
    api_instance = openapi_client.SecureOutboundPaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    payment_request_detail_dto = openapi_client.PaymentRequestDetailDTO() # PaymentRequestDetailDTO | PaymentRequestDetailDTO

    try:
        # This API fetch outbound payment by paymentId
        api_response = api_instance.vendorapi_secure_outboundpayments_detail_post(x_api_key, x_app_key, x_version, origin, payment_request_detail_dto)
        print("The response of SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_detail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_detail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **payment_request_detail_dto** | [**PaymentRequestDetailDTO**](PaymentRequestDetailDTO.md)| PaymentRequestDetailDTO | 

### Return type

[**PaymentDetailResponseDTO**](PaymentDetailResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

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

# **vendorapi_secure_outboundpayments_post**
> PaymentResponseDto vendorapi_secure_outboundpayments_post(x_api_key, x_app_key, x_version, origin, payment_request_dto)

This API creates outbound payment request

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.payment_request_dto import PaymentRequestDto
from openapi_client.models.payment_response_dto import PaymentResponseDto
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
    api_instance = openapi_client.SecureOutboundPaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    payment_request_dto = openapi_client.PaymentRequestDto() # PaymentRequestDto | PaymentRequestDto

    try:
        # This API creates outbound payment request
        api_response = api_instance.vendorapi_secure_outboundpayments_post(x_api_key, x_app_key, x_version, origin, payment_request_dto)
        print("The response of SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **payment_request_dto** | [**PaymentRequestDto**](PaymentRequestDto.md)| PaymentRequestDto | 

### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PaymentResponseDto |  -  |
**400** | Bad request or validation error |  -  |
**404** | Merchant not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_outboundpayments_search_post**
> PagePaymentListResponseDTO vendorapi_secure_outboundpayments_search_post(x_api_key, x_app_key, x_version, origin, vendor_id=vendor_id, payment_based_id=payment_based_id, payment_id=payment_id, vendor_name=vendor_name, payment_method_type=payment_method_type, payment_method_status=payment_method_status, amount=amount, from_amount=from_amount, to_amount=to_amount, start_date=start_date, end_date=end_date, search_text=search_text, sort_field=sort_field)

This API gets all outbound payment

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.page_payment_list_response_dto import PagePaymentListResponseDTO
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
    api_instance = openapi_client.SecureOutboundPaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    vendor_id = 'vendor_id_example' # str | sets vendorId (optional)
    payment_based_id = 'payment_based_id_example' # str | sets paymentBasedId (optional)
    payment_id = 'payment_id_example' # str | sets paymentId (optional)
    vendor_name = 'vendor_name_example' # str | sets vendorName (optional)
    payment_method_type = 'payment_method_type_example' # str | sets paymentMethodType (optional)
    payment_method_status = 'payment_method_status_example' # str | sets paymentMethodStatus (optional)
    amount = 3.4 # float | sets amount (optional)
    from_amount = 3.4 # float | sets fromAmount (optional)
    to_amount = 3.4 # float | sets toAmount (optional)
    start_date = 'start_date_example' # str | sets startDate (optional)
    end_date = 'end_date_example' # str | sets endDate (optional)
    search_text = 'search_text_example' # str | sets searchText (optional)
    sort_field = 'sort_field_example' # str | sets sortField (optional)

    try:
        # This API gets all outbound payment
        api_response = api_instance.vendorapi_secure_outboundpayments_search_post(x_api_key, x_app_key, x_version, origin, vendor_id=vendor_id, payment_based_id=payment_based_id, payment_id=payment_id, vendor_name=vendor_name, payment_method_type=payment_method_type, payment_method_status=payment_method_status, amount=amount, from_amount=from_amount, to_amount=to_amount, start_date=start_date, end_date=end_date, search_text=search_text, sort_field=sort_field)
        print("The response of SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureOutboundPaymentsApi->vendorapi_secure_outboundpayments_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **vendor_id** | **str**| sets vendorId | [optional] 
 **payment_based_id** | **str**| sets paymentBasedId | [optional] 
 **payment_id** | **str**| sets paymentId | [optional] 
 **vendor_name** | **str**| sets vendorName | [optional] 
 **payment_method_type** | **str**| sets paymentMethodType | [optional] 
 **payment_method_status** | **str**| sets paymentMethodStatus | [optional] 
 **amount** | **float**| sets amount | [optional] 
 **from_amount** | **float**| sets fromAmount | [optional] 
 **to_amount** | **float**| sets toAmount | [optional] 
 **start_date** | **str**| sets startDate | [optional] 
 **end_date** | **str**| sets endDate | [optional] 
 **search_text** | **str**| sets searchText | [optional] 
 **sort_field** | **str**| sets sortField | [optional] 

### Return type

[**PagePaymentListResponseDTO**](PagePaymentListResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OutboundPayments searched successfully |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

