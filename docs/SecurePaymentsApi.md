# openapi_client.SecurePaymentsApi

All URIs are relative to *https://api.uat.anddone.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secure_payments_export_post**](SecurePaymentsApi.md#secure_payments_export_post) | **POST** /secure/payments/export | This API gets Secure payment by search criteria for the merchant.
[**secure_payments_post**](SecurePaymentsApi.md#secure_payments_post) | **POST** /secure/payments | This API posts new Secure payment request for the merchant.
[**secure_payments_search_post**](SecurePaymentsApi.md#secure_payments_search_post) | **POST** /secure/payments/search | This API gets Secure payment by search criteria for the merchant.
[**secure_paymentsdetails_post**](SecurePaymentsApi.md#secure_paymentsdetails_post) | **POST** /secure/paymentsdetails | This API is used for getting details of Payments


# **secure_payments_export_post**
> secure_payments_export_post(x_api_key, x_app_key, x_version, origin, start_date=start_date, end_date=end_date, transaction_ids=transaction_ids, reference_transaction_id=reference_transaction_id, transaction_statuses=transaction_statuses, customer_ids=customer_ids, transaction_type=transaction_type, auth_code=auth_code, card_holder_name=card_holder_name, shopper_name=shopper_name, amount=amount, from_amount=from_amount, to_amount=to_amount, channel_types=channel_types, mask_account=mask_account, customer_name=customer_name, recurring_id=recurring_id, reference_no=reference_no, export_to_csv=export_to_csv, export_to_pdf=export_to_pdf, transaction_origins=transaction_origins, transaction_source_type=transaction_source_type, source_id=source_id, trace_numbers=trace_numbers, bin_number=bin_number, process_method=process_method, search_text=search_text, merchant_reference=merchant_reference, additional_fields=additional_fields, additional_field_value=additional_field_value, payment_method=payment_method, account_alias=account_alias, is_paid=is_paid, payment_types=payment_types, merchant_id=merchant_id, payment_categories=payment_categories, suppress_technology_fee=suppress_technology_fee, batch_id=batch_id, sort_field=sort_field, start_row=start_row, page_size=page_size, asc=asc)

This API gets Secure payment by search criteria for the merchant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.SecurePaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    start_date = 'start_date_example' # str | Start date for the transaction search (optional)
    end_date = 'end_date_example' # str | End date for the transaction search (optional)
    transaction_ids = 'transaction_ids_example' # str | Transaction identifier (optional)
    reference_transaction_id = 'reference_transaction_id_example' # str | Reference transaction identifier (optional)
    transaction_statuses = 'transaction_statuses_example' # str | Status of the transaction (optional)
    customer_ids = 'customer_ids_example' # str | Customer IDs associated with the transaction (optional)
    transaction_type = 'transaction_type_example' # str | Type of the transaction (optional)
    auth_code = 'auth_code_example' # str | Authorization code of the transaction (optional)
    card_holder_name = 'card_holder_name_example' # str | Name of the cardholder (optional)
    shopper_name = 'shopper_name_example' # str | ShopperName of the cardholder (optional)
    amount = 3.4 # float | Transaction amount (optional)
    from_amount = 3.4 # float | Minimum transaction amount (optional)
    to_amount = 3.4 # float | Maximum transaction amount (optional)
    channel_types = 'channel_types_example' # str | Channel types used for the transaction (optional)
    mask_account = 'mask_account_example' # str | Masked account number (optional)
    customer_name = 'customer_name_example' # str | Name of the customer (optional)
    recurring_id = 'recurring_id_example' # str | Recurring payment ID (optional)
    reference_no = 'reference_no_example' # str | Reference number (optional)
    export_to_csv = True # bool | Export To Csv (optional)
    export_to_pdf = True # bool | Export To PDF (optional)
    transaction_origins = 'transaction_origins_example' # str | Type of origin used in the transaction (optional)
    transaction_source_type = 'transaction_source_type_example' # str | Transaction source type of the transaction (optional)
    source_id = 56 # int | Set SourceId (optional)
    trace_numbers = 'trace_numbers_example' # str | TraceNumbers associated with the transaction (optional)
    bin_number = 'bin_number_example' # str | BinNumber (optional)
    process_method = 'process_method_example' # str | Process Method used for the transaction (optional)
    search_text = 'search_text_example' # str | SearchText of the transaction (optional)
    merchant_reference = 'merchant_reference_example' # str | Merchant Reference of the transaction (optional)
    additional_fields = 'additional_fields_example' # str | Additional Fields (optional)
    additional_field_value = 'additional_field_value_example' # str | AdditionalFieldValue (optional)
    payment_method = 'payment_method_example' # str | Payment Method (optional)
    account_alias = 'account_alias_example' # str | Set AccountAlias (optional)
    is_paid = True # bool | Set IsPaid (optional)
    payment_types = 'payment_types_example' # str | Type of payment used in the transaction (optional)
    merchant_id = 'merchant_id_example' # str | Search with Merchant Id (optional)
    payment_categories = 'payment_categories_example' # str | Set PaymentCategories (optional)
    suppress_technology_fee = True # bool | SuppressTechnologyFee (optional)
    batch_id = 'batch_id_example' # str | BatchId (optional)
    sort_field = 'sort_field_example' # str | SortField (optional)
    start_row = 56 # int | Set StartRow (optional)
    page_size = 56 # int | Set PageSize (optional)
    asc = True # bool | Set Asc (optional)

    try:
        # This API gets Secure payment by search criteria for the merchant.
        api_instance.secure_payments_export_post(x_api_key, x_app_key, x_version, origin, start_date=start_date, end_date=end_date, transaction_ids=transaction_ids, reference_transaction_id=reference_transaction_id, transaction_statuses=transaction_statuses, customer_ids=customer_ids, transaction_type=transaction_type, auth_code=auth_code, card_holder_name=card_holder_name, shopper_name=shopper_name, amount=amount, from_amount=from_amount, to_amount=to_amount, channel_types=channel_types, mask_account=mask_account, customer_name=customer_name, recurring_id=recurring_id, reference_no=reference_no, export_to_csv=export_to_csv, export_to_pdf=export_to_pdf, transaction_origins=transaction_origins, transaction_source_type=transaction_source_type, source_id=source_id, trace_numbers=trace_numbers, bin_number=bin_number, process_method=process_method, search_text=search_text, merchant_reference=merchant_reference, additional_fields=additional_fields, additional_field_value=additional_field_value, payment_method=payment_method, account_alias=account_alias, is_paid=is_paid, payment_types=payment_types, merchant_id=merchant_id, payment_categories=payment_categories, suppress_technology_fee=suppress_technology_fee, batch_id=batch_id, sort_field=sort_field, start_row=start_row, page_size=page_size, asc=asc)
    except Exception as e:
        print("Exception when calling SecurePaymentsApi->secure_payments_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **start_date** | **str**| Start date for the transaction search | [optional] 
 **end_date** | **str**| End date for the transaction search | [optional] 
 **transaction_ids** | **str**| Transaction identifier | [optional] 
 **reference_transaction_id** | **str**| Reference transaction identifier | [optional] 
 **transaction_statuses** | **str**| Status of the transaction | [optional] 
 **customer_ids** | **str**| Customer IDs associated with the transaction | [optional] 
 **transaction_type** | **str**| Type of the transaction | [optional] 
 **auth_code** | **str**| Authorization code of the transaction | [optional] 
 **card_holder_name** | **str**| Name of the cardholder | [optional] 
 **shopper_name** | **str**| ShopperName of the cardholder | [optional] 
 **amount** | **float**| Transaction amount | [optional] 
 **from_amount** | **float**| Minimum transaction amount | [optional] 
 **to_amount** | **float**| Maximum transaction amount | [optional] 
 **channel_types** | **str**| Channel types used for the transaction | [optional] 
 **mask_account** | **str**| Masked account number | [optional] 
 **customer_name** | **str**| Name of the customer | [optional] 
 **recurring_id** | **str**| Recurring payment ID | [optional] 
 **reference_no** | **str**| Reference number | [optional] 
 **export_to_csv** | **bool**| Export To Csv | [optional] 
 **export_to_pdf** | **bool**| Export To PDF | [optional] 
 **transaction_origins** | **str**| Type of origin used in the transaction | [optional] 
 **transaction_source_type** | **str**| Transaction source type of the transaction | [optional] 
 **source_id** | **int**| Set SourceId | [optional] 
 **trace_numbers** | **str**| TraceNumbers associated with the transaction | [optional] 
 **bin_number** | **str**| BinNumber | [optional] 
 **process_method** | **str**| Process Method used for the transaction | [optional] 
 **search_text** | **str**| SearchText of the transaction | [optional] 
 **merchant_reference** | **str**| Merchant Reference of the transaction | [optional] 
 **additional_fields** | **str**| Additional Fields | [optional] 
 **additional_field_value** | **str**| AdditionalFieldValue | [optional] 
 **payment_method** | **str**| Payment Method | [optional] 
 **account_alias** | **str**| Set AccountAlias | [optional] 
 **is_paid** | **bool**| Set IsPaid | [optional] 
 **payment_types** | **str**| Type of payment used in the transaction | [optional] 
 **merchant_id** | **str**| Search with Merchant Id | [optional] 
 **payment_categories** | **str**| Set PaymentCategories | [optional] 
 **suppress_technology_fee** | **bool**| SuppressTechnologyFee | [optional] 
 **batch_id** | **str**| BatchId | [optional] 
 **sort_field** | **str**| SortField | [optional] 
 **start_row** | **int**| Set StartRow | [optional] 
 **page_size** | **int**| Set PageSize | [optional] 
 **asc** | **bool**| Set Asc | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation - SSE stream initiated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secure_payments_post**
> TransactionDetailResponse secure_payments_post(x_api_key, x_app_key, x_version, origin, payment_request)

This API posts new Secure payment request for the merchant.

### Example


```python
import openapi_client
from openapi_client.models.payment_request import PaymentRequest
from openapi_client.models.transaction_detail_response import TransactionDetailResponse
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
    api_instance = openapi_client.SecurePaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    payment_request = openapi_client.PaymentRequest() # PaymentRequest | Payment Detail

    try:
        # This API posts new Secure payment request for the merchant.
        api_response = api_instance.secure_payments_post(x_api_key, x_app_key, x_version, origin, payment_request)
        print("The response of SecurePaymentsApi->secure_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentsApi->secure_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **payment_request** | [**PaymentRequest**](PaymentRequest.md)| Payment Detail | 

### Return type

[**TransactionDetailResponse**](TransactionDetailResponse.md)

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

# **secure_payments_search_post**
> MerchantTransactionEntityResponse secure_payments_search_post(x_api_key, x_app_key, x_version, origin, start_date=start_date, end_date=end_date, transaction_ids=transaction_ids, reference_transaction_id=reference_transaction_id, transaction_statuses=transaction_statuses, customer_ids=customer_ids, transaction_type=transaction_type, auth_code=auth_code, card_holder_name=card_holder_name, shopper_name=shopper_name, amount=amount, from_amount=from_amount, to_amount=to_amount, channel_types=channel_types, mask_account=mask_account, customer_name=customer_name, recurring_id=recurring_id, reference_no=reference_no, export_to_csv=export_to_csv, export_to_pdf=export_to_pdf, transaction_origins=transaction_origins, transaction_source_type=transaction_source_type, source_id=source_id, trace_numbers=trace_numbers, bin_number=bin_number, process_method=process_method, search_text=search_text, merchant_reference=merchant_reference, additional_fields=additional_fields, additional_field_value=additional_field_value, payment_method=payment_method, account_alias=account_alias, is_paid=is_paid, payment_types=payment_types, merchant_id=merchant_id, payment_categories=payment_categories, suppress_technology_fee=suppress_technology_fee, batch_id=batch_id, transactions_count=transactions_count, sort_field=sort_field, start_row=start_row, page_size=page_size, asc=asc)

This API gets Secure payment by search criteria for the merchant.

### Example


```python
import openapi_client
from openapi_client.models.merchant_transaction_entity_response import MerchantTransactionEntityResponse
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
    api_instance = openapi_client.SecurePaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    start_date = 'start_date_example' # str | Start date for the transaction search (optional)
    end_date = 'end_date_example' # str | End date for the transaction search (optional)
    transaction_ids = 'transaction_ids_example' # str | Transaction identifier (optional)
    reference_transaction_id = 'reference_transaction_id_example' # str | Reference transaction identifier (optional)
    transaction_statuses = 'transaction_statuses_example' # str | Status of the transaction (optional)
    customer_ids = 'customer_ids_example' # str | Customer IDs associated with the transaction (optional)
    transaction_type = 'transaction_type_example' # str | Type of the transaction (optional)
    auth_code = 'auth_code_example' # str | Authorization code of the transaction (optional)
    card_holder_name = 'card_holder_name_example' # str | Name of the cardholder (optional)
    shopper_name = 'shopper_name_example' # str | ShopperName of the cardholder (optional)
    amount = 3.4 # float | Transaction amount (optional)
    from_amount = 3.4 # float | Minimum transaction amount (optional)
    to_amount = 3.4 # float | Maximum transaction amount (optional)
    channel_types = 'channel_types_example' # str | Channel types used for the transaction (optional)
    mask_account = 'mask_account_example' # str | Masked account number (optional)
    customer_name = 'customer_name_example' # str | Name of the customer (optional)
    recurring_id = 'recurring_id_example' # str | Recurring payment ID (optional)
    reference_no = 'reference_no_example' # str | Reference number (optional)
    export_to_csv = True # bool | Export To Csv (optional)
    export_to_pdf = True # bool | Export To PDF (optional)
    transaction_origins = 'transaction_origins_example' # str | Type of origin used in the transaction (optional)
    transaction_source_type = 'transaction_source_type_example' # str | Transaction source type of the transaction (optional)
    source_id = 56 # int | Set SourceId (optional)
    trace_numbers = 'trace_numbers_example' # str | TraceNumbers associated with the transaction (optional)
    bin_number = 'bin_number_example' # str | BinNumber (optional)
    process_method = 'process_method_example' # str | Process Method used for the transaction (optional)
    search_text = 'search_text_example' # str | SearchText of the transaction (optional)
    merchant_reference = 'merchant_reference_example' # str | Merchant Reference of the transaction (optional)
    additional_fields = 'additional_fields_example' # str | Additional Fields (optional)
    additional_field_value = 'additional_field_value_example' # str | AdditionalFieldValue (optional)
    payment_method = 'payment_method_example' # str | Payment Method (optional)
    account_alias = 'account_alias_example' # str | Set AccountAlias (optional)
    is_paid = True # bool | Set IsPaid (optional)
    payment_types = 'payment_types_example' # str | Type of payment used in the transaction (optional)
    merchant_id = 'merchant_id_example' # str | Search with Merchant Id (optional)
    payment_categories = 'payment_categories_example' # str | Set PaymentCategories (optional)
    suppress_technology_fee = True # bool | SuppressTechnologyFee (optional)
    batch_id = 'batch_id_example' # str | BatchId (optional)
    transactions_count = True # bool | Set whether to return only the transactions count (optional)
    sort_field = 'sort_field_example' # str | SortField (optional)
    start_row = 56 # int | Set StartRow (optional)
    page_size = 56 # int | Set PageSize (optional)
    asc = True # bool | Set Asc (optional)

    try:
        # This API gets Secure payment by search criteria for the merchant.
        api_response = api_instance.secure_payments_search_post(x_api_key, x_app_key, x_version, origin, start_date=start_date, end_date=end_date, transaction_ids=transaction_ids, reference_transaction_id=reference_transaction_id, transaction_statuses=transaction_statuses, customer_ids=customer_ids, transaction_type=transaction_type, auth_code=auth_code, card_holder_name=card_holder_name, shopper_name=shopper_name, amount=amount, from_amount=from_amount, to_amount=to_amount, channel_types=channel_types, mask_account=mask_account, customer_name=customer_name, recurring_id=recurring_id, reference_no=reference_no, export_to_csv=export_to_csv, export_to_pdf=export_to_pdf, transaction_origins=transaction_origins, transaction_source_type=transaction_source_type, source_id=source_id, trace_numbers=trace_numbers, bin_number=bin_number, process_method=process_method, search_text=search_text, merchant_reference=merchant_reference, additional_fields=additional_fields, additional_field_value=additional_field_value, payment_method=payment_method, account_alias=account_alias, is_paid=is_paid, payment_types=payment_types, merchant_id=merchant_id, payment_categories=payment_categories, suppress_technology_fee=suppress_technology_fee, batch_id=batch_id, transactions_count=transactions_count, sort_field=sort_field, start_row=start_row, page_size=page_size, asc=asc)
        print("The response of SecurePaymentsApi->secure_payments_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentsApi->secure_payments_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **start_date** | **str**| Start date for the transaction search | [optional] 
 **end_date** | **str**| End date for the transaction search | [optional] 
 **transaction_ids** | **str**| Transaction identifier | [optional] 
 **reference_transaction_id** | **str**| Reference transaction identifier | [optional] 
 **transaction_statuses** | **str**| Status of the transaction | [optional] 
 **customer_ids** | **str**| Customer IDs associated with the transaction | [optional] 
 **transaction_type** | **str**| Type of the transaction | [optional] 
 **auth_code** | **str**| Authorization code of the transaction | [optional] 
 **card_holder_name** | **str**| Name of the cardholder | [optional] 
 **shopper_name** | **str**| ShopperName of the cardholder | [optional] 
 **amount** | **float**| Transaction amount | [optional] 
 **from_amount** | **float**| Minimum transaction amount | [optional] 
 **to_amount** | **float**| Maximum transaction amount | [optional] 
 **channel_types** | **str**| Channel types used for the transaction | [optional] 
 **mask_account** | **str**| Masked account number | [optional] 
 **customer_name** | **str**| Name of the customer | [optional] 
 **recurring_id** | **str**| Recurring payment ID | [optional] 
 **reference_no** | **str**| Reference number | [optional] 
 **export_to_csv** | **bool**| Export To Csv | [optional] 
 **export_to_pdf** | **bool**| Export To PDF | [optional] 
 **transaction_origins** | **str**| Type of origin used in the transaction | [optional] 
 **transaction_source_type** | **str**| Transaction source type of the transaction | [optional] 
 **source_id** | **int**| Set SourceId | [optional] 
 **trace_numbers** | **str**| TraceNumbers associated with the transaction | [optional] 
 **bin_number** | **str**| BinNumber | [optional] 
 **process_method** | **str**| Process Method used for the transaction | [optional] 
 **search_text** | **str**| SearchText of the transaction | [optional] 
 **merchant_reference** | **str**| Merchant Reference of the transaction | [optional] 
 **additional_fields** | **str**| Additional Fields | [optional] 
 **additional_field_value** | **str**| AdditionalFieldValue | [optional] 
 **payment_method** | **str**| Payment Method | [optional] 
 **account_alias** | **str**| Set AccountAlias | [optional] 
 **is_paid** | **bool**| Set IsPaid | [optional] 
 **payment_types** | **str**| Type of payment used in the transaction | [optional] 
 **merchant_id** | **str**| Search with Merchant Id | [optional] 
 **payment_categories** | **str**| Set PaymentCategories | [optional] 
 **suppress_technology_fee** | **bool**| SuppressTechnologyFee | [optional] 
 **batch_id** | **str**| BatchId | [optional] 
 **transactions_count** | **bool**| Set whether to return only the transactions count | [optional] 
 **sort_field** | **str**| SortField | [optional] 
 **start_row** | **int**| Set StartRow | [optional] 
 **page_size** | **int**| Set PageSize | [optional] 
 **asc** | **bool**| Set Asc | [optional] 

### Return type

[**MerchantTransactionEntityResponse**](MerchantTransactionEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secure_paymentsdetails_post**
> TransactionPaymentResponse secure_paymentsdetails_post(x_api_key, x_app_key, x_version, origin, secure_payment_details_request)

This API is used for getting details of Payments

### Example


```python
import openapi_client
from openapi_client.models.secure_payment_details_request import SecurePaymentDetailsRequest
from openapi_client.models.transaction_payment_response import TransactionPaymentResponse
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
    api_instance = openapi_client.SecurePaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | an authorization header
    x_app_key = 'x_app_key_example' # str | an authorization header
    x_version = 'x_version_example' # str | x-version
    origin = 'origin_example' # str | origin
    secure_payment_details_request = openapi_client.SecurePaymentDetailsRequest() # SecurePaymentDetailsRequest | Payment Details Request

    try:
        # This API is used for getting details of Payments
        api_response = api_instance.secure_paymentsdetails_post(x_api_key, x_app_key, x_version, origin, secure_payment_details_request)
        print("The response of SecurePaymentsApi->secure_paymentsdetails_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurePaymentsApi->secure_paymentsdetails_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| an authorization header | 
 **x_app_key** | **str**| an authorization header | 
 **x_version** | **str**| x-version | 
 **origin** | **str**| origin | 
 **secure_payment_details_request** | [**SecurePaymentDetailsRequest**](SecurePaymentDetailsRequest.md)| Payment Details Request | 

### Return type

[**TransactionPaymentResponse**](TransactionPaymentResponse.md)

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

