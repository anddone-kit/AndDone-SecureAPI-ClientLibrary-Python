# openapi_client.SecureVendorManagementApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendorapi_secure_merchants_vendors_delete_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_delete_post) | **POST** /vendorapi/secure/merchants/vendors/delete | This API deletes vendor into system
[**vendorapi_secure_merchants_vendors_details_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_details_post) | **POST** /vendorapi/secure/merchants/vendors/details | This API gets details of particular vendor
[**vendorapi_secure_merchants_vendors_edit_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_edit_post) | **POST** /vendorapi/secure/merchants/vendors/edit | This API Updates the existing vendor
[**vendorapi_secure_merchants_vendors_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_post) | **POST** /vendorapi/secure/merchants/vendors | This API creates vendor into system
[**vendorapi_secure_merchants_vendors_search_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_search_post) | **POST** /vendorapi/secure/merchants/vendors/search | This API returns list of all the Vendors of Merchant
[**vendorapi_secure_merchants_vendors_suspend_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_suspend_post) | **POST** /vendorapi/secure/merchants/vendors/suspend | This API suspends vendor into system
[**vendorapi_secure_merchants_vendors_timeline_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_timeline_post) | **POST** /vendorapi/secure/merchants/vendors/timeline | This API gets timeline of particular vendor
[**vendorapi_secure_merchants_vendors_unsuspend_post**](SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_unsuspend_post) | **POST** /vendorapi/secure/merchants/vendors/unsuspend | This API unsuspends vendor into system


# **vendorapi_secure_merchants_vendors_delete_post**
> vendorapi_secure_merchants_vendors_delete_post(x_api_key, x_app_key, x_version, origin, secure_vendor_status_request_dto)

This API deletes vendor into system

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_status_request_dto import SecureVendorStatusRequestDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_vendor_status_request_dto = openapi_client.SecureVendorStatusRequestDTO() # SecureVendorStatusRequestDTO | SecureVendorStatusRequestDTO

    try:
        # This API deletes vendor into system
        api_instance.vendorapi_secure_merchants_vendors_delete_post(x_api_key, x_app_key, x_version, origin, secure_vendor_status_request_dto)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_vendor_status_request_dto** | [**SecureVendorStatusRequestDTO**](SecureVendorStatusRequestDTO.md)| SecureVendorStatusRequestDTO | 

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
**200** | Vendor deleted successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_details_post**
> VendorResponseDTO vendorapi_secure_merchants_vendors_details_post(x_api_key, x_app_key, x_version, origin, secure_vendor_request_dto)

This API gets details of particular vendor

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_request_dto import SecureVendorRequestDTO
from openapi_client.models.vendor_response_dto import VendorResponseDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_vendor_request_dto = openapi_client.SecureVendorRequestDTO() # SecureVendorRequestDTO | SecureVendorRequestDTO

    try:
        # This API gets details of particular vendor
        api_response = api_instance.vendorapi_secure_merchants_vendors_details_post(x_api_key, x_app_key, x_version, origin, secure_vendor_request_dto)
        print("The response of SecureVendorManagementApi->vendorapi_secure_merchants_vendors_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_vendor_request_dto** | [**SecureVendorRequestDTO**](SecureVendorRequestDTO.md)| SecureVendorRequestDTO | 

### Return type

[**VendorResponseDTO**](VendorResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor details fetched successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_edit_post**
> SecureVendorResponseDTO vendorapi_secure_merchants_vendors_edit_post(x_api_key, x_app_key, x_version, origin, secure_vendor_update_request_dto)

This API Updates the existing vendor

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_response_dto import SecureVendorResponseDTO
from openapi_client.models.secure_vendor_update_request_dto import SecureVendorUpdateRequestDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_vendor_update_request_dto = openapi_client.SecureVendorUpdateRequestDTO() # SecureVendorUpdateRequestDTO | SecureVendorUpdateRequestDTO

    try:
        # This API Updates the existing vendor
        api_response = api_instance.vendorapi_secure_merchants_vendors_edit_post(x_api_key, x_app_key, x_version, origin, secure_vendor_update_request_dto)
        print("The response of SecureVendorManagementApi->vendorapi_secure_merchants_vendors_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_vendor_update_request_dto** | [**SecureVendorUpdateRequestDTO**](SecureVendorUpdateRequestDTO.md)| SecureVendorUpdateRequestDTO | 

### Return type

[**SecureVendorResponseDTO**](SecureVendorResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor updated successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_post**
> SecureVendorResponseDTO vendorapi_secure_merchants_vendors_post(x_api_key, x_app_key, x_version, origin, vendor_request_dto)

This API creates vendor into system

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_response_dto import SecureVendorResponseDTO
from openapi_client.models.vendor_request_dto import VendorRequestDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    vendor_request_dto = openapi_client.VendorRequestDTO() # VendorRequestDTO | VendorRequestDTO

    try:
        # This API creates vendor into system
        api_response = api_instance.vendorapi_secure_merchants_vendors_post(x_api_key, x_app_key, x_version, origin, vendor_request_dto)
        print("The response of SecureVendorManagementApi->vendorapi_secure_merchants_vendors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **vendor_request_dto** | [**VendorRequestDTO**](VendorRequestDTO.md)| VendorRequestDTO | 

### Return type

[**SecureVendorResponseDTO**](SecureVendorResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecureVendorResponseDTO |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_search_post**
> PageVendorResponseDTO vendorapi_secure_merchants_vendors_search_post(x_api_key, x_app_key, x_version, origin, payment_method_type=payment_method_type, attention=attention, vendor_id=vendor_id, vendor_name=vendor_name, vendor_status=vendor_status, created_by=created_by, start_date=start_date, end_date=end_date, page_size=page_size, search_text=search_text, sort_field=sort_field, start_row=start_row, asc=asc)

This API returns list of all the Vendors of Merchant

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.page_vendor_response_dto import PageVendorResponseDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    payment_method_type = 'payment_method_type_example' # str | Set paymentMethodType (optional)
    attention = 'attention_example' # str | Set attention (optional)
    vendor_id = 'vendor_id_example' # str | Set vendorId (optional)
    vendor_name = 'vendor_name_example' # str | Set vendorName (optional)
    vendor_status = 'vendor_status_example' # str | Set vendorStatus (optional)
    created_by = 'created_by_example' # str | Set createdBy (optional)
    start_date = 'start_date_example' # str | set start Date (optional)
    end_date = 'end_date_example' # str | set end Date (optional)
    page_size = 3.4 # float | Set PageSize (optional)
    search_text = 'search_text_example' # str | search Text (optional)
    sort_field = 'sort_field_example' # str | Set SortField (optional)
    start_row = 'start_row_example' # str | Set StartRow (optional)
    asc = True # bool | Set Asc (optional)

    try:
        # This API returns list of all the Vendors of Merchant
        api_response = api_instance.vendorapi_secure_merchants_vendors_search_post(x_api_key, x_app_key, x_version, origin, payment_method_type=payment_method_type, attention=attention, vendor_id=vendor_id, vendor_name=vendor_name, vendor_status=vendor_status, created_by=created_by, start_date=start_date, end_date=end_date, page_size=page_size, search_text=search_text, sort_field=sort_field, start_row=start_row, asc=asc)
        print("The response of SecureVendorManagementApi->vendorapi_secure_merchants_vendors_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **payment_method_type** | **str**| Set paymentMethodType | [optional] 
 **attention** | **str**| Set attention | [optional] 
 **vendor_id** | **str**| Set vendorId | [optional] 
 **vendor_name** | **str**| Set vendorName | [optional] 
 **vendor_status** | **str**| Set vendorStatus | [optional] 
 **created_by** | **str**| Set createdBy | [optional] 
 **start_date** | **str**| set start Date | [optional] 
 **end_date** | **str**| set end Date | [optional] 
 **page_size** | **float**| Set PageSize | [optional] 
 **search_text** | **str**| search Text | [optional] 
 **sort_field** | **str**| Set SortField | [optional] 
 **start_row** | **str**| Set StartRow | [optional] 
 **asc** | **bool**| Set Asc | [optional] 

### Return type

[**PageVendorResponseDTO**](PageVendorResponseDTO.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor searched successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_suspend_post**
> vendorapi_secure_merchants_vendors_suspend_post(x_api_key, x_app_key, x_version, origin, secure_vendor_status_request_dto)

This API suspends vendor into system

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_status_request_dto import SecureVendorStatusRequestDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_vendor_status_request_dto = openapi_client.SecureVendorStatusRequestDTO() # SecureVendorStatusRequestDTO | SecureVendorStatusRequestDTO

    try:
        # This API suspends vendor into system
        api_instance.vendorapi_secure_merchants_vendors_suspend_post(x_api_key, x_app_key, x_version, origin, secure_vendor_status_request_dto)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_suspend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_vendor_status_request_dto** | [**SecureVendorStatusRequestDTO**](SecureVendorStatusRequestDTO.md)| SecureVendorStatusRequestDTO | 

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
**200** | Vendor suspended successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_timeline_post**
> List[VendorTimelineResponseListInner] vendorapi_secure_merchants_vendors_timeline_post(x_api_key, x_app_key, x_version, origin, secure_vendor_timeline_request_dto)

This API gets timeline of particular vendor

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_timeline_request_dto import SecureVendorTimelineRequestDTO
from openapi_client.models.vendor_timeline_response_list_inner import VendorTimelineResponseListInner
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_vendor_timeline_request_dto = openapi_client.SecureVendorTimelineRequestDTO() # SecureVendorTimelineRequestDTO | SecureVendorTimelineRequestDTO

    try:
        # This API gets timeline of particular vendor
        api_response = api_instance.vendorapi_secure_merchants_vendors_timeline_post(x_api_key, x_app_key, x_version, origin, secure_vendor_timeline_request_dto)
        print("The response of SecureVendorManagementApi->vendorapi_secure_merchants_vendors_timeline_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_timeline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_vendor_timeline_request_dto** | [**SecureVendorTimelineRequestDTO**](SecureVendorTimelineRequestDTO.md)| SecureVendorTimelineRequestDTO | 

### Return type

[**List[VendorTimelineResponseListInner]**](VendorTimelineResponseListInner.md)

### Authorization

[x-api-key](../README.md#x-api-key), [x-app-key](../README.md#x-app-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor timeline fetched successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendorapi_secure_merchants_vendors_unsuspend_post**
> vendorapi_secure_merchants_vendors_unsuspend_post(x_api_key, x_app_key, x_version, origin, secure_vendor_status_request_dto)

This API unsuspends vendor into system

### Example

* Api Key Authentication (x-api-key):
* Api Key Authentication (x-app-key):

```python
import openapi_client
from openapi_client.models.secure_vendor_status_request_dto import SecureVendorStatusRequestDTO
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
    api_instance = openapi_client.SecureVendorManagementApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_vendor_status_request_dto = openapi_client.SecureVendorStatusRequestDTO() # SecureVendorStatusRequestDTO | SecureVendorStatusRequestDTO

    try:
        # This API unsuspends vendor into system
        api_instance.vendorapi_secure_merchants_vendors_unsuspend_post(x_api_key, x_app_key, x_version, origin, secure_vendor_status_request_dto)
    except Exception as e:
        print("Exception when calling SecureVendorManagementApi->vendorapi_secure_merchants_vendors_unsuspend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_vendor_status_request_dto** | [**SecureVendorStatusRequestDTO**](SecureVendorStatusRequestDTO.md)| SecureVendorStatusRequestDTO | 

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
**200** | Vendor unsuspended successfully |  -  |
**400** | Bad request or validation error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

