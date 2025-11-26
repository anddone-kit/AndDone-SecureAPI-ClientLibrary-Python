# openapi_client.SecureReportsApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_reports_downloads_post**](SecureReportsApi.md#secure_reports_downloads_post) | **POST** /secure/reports/downloads | This API will add system report.


# **secure_reports_downloads_post**
> secure_reports_downloads_post(x_api_key, x_app_key, x_version, origin, report_download_request=report_download_request)

This API will add system report.

### Example


```python
import openapi_client
from openapi_client.models.report_download_request import ReportDownloadRequest
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
    api_instance = openapi_client.SecureReportsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    report_download_request = openapi_client.ReportDownloadRequest() # ReportDownloadRequest | ReportDownloadRequest (optional)

    try:
        # This API will add system report.
        api_instance.secure_reports_downloads_post(x_api_key, x_app_key, x_version, origin, report_download_request=report_download_request)
    except Exception as e:
        print("Exception when calling SecureReportsApi->secure_reports_downloads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **report_download_request** | [**ReportDownloadRequest**](ReportDownloadRequest.md)| ReportDownloadRequest | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful CSV file download |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

