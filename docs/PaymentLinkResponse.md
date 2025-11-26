# PaymentLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**payment_link** | **str** |  | [optional] 
**short_link** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**payment_description** | **str** |  | [optional] 
**expire_in** | **int** |  | [optional] 
**expire_in_unit** | **str** |  | [optional] 
**expire_on** | **str** |  | [optional] 
**payments** | [**List[PaymentLinkResponsePaymentsInner]**](PaymentLinkResponsePaymentsInner.md) |  | [optional] 
**no_of_payment_made** | **int** |  | [optional] 
**total_paid_amount** | **float** |  | [optional] 
**link_status** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**response_type** | **str** |  | [optional] 
**callback_parameters** | [**PaymentLinkResponseCallbackParameters**](PaymentLinkResponseCallbackParameters.md) |  | [optional] 
**customers** | [**List[PaymentLinkResponseCustomersInner]**](PaymentLinkResponseCustomersInner.md) |  | [optional] 
**line_items** | [**List[PaymentLinkResponseLineItemsInner]**](PaymentLinkResponseLineItemsInner.md) |  | [optional] 
**display_settings** | [**PaymentLinkResponseDisplaySettings**](PaymentLinkResponseDisplaySettings.md) |  | [optional] 
**splits** | [**List[PaymentIntentRequestSplitsInner]**](PaymentIntentRequestSplitsInner.md) |  | [optional] 
**save_for_future** | **bool** |  | [optional] 
**quote_key** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reference_key** | **str** |  | [optional] 
**reference_data_list** | [**List[PaymentLinkResponseReferenceDataListInner]**](PaymentLinkResponseReferenceDataListInner.md) |  | [optional] 
**enable_premium_finance** | **bool** |  | [optional] 
**is_premium_financier** | **bool** |  | [optional] 
**pfr** | [**PaymentIntentRequestPfr**](PaymentIntentRequestPfr.md) |  | [optional] 
**payment_link_type** | **str** |  | [optional] 
**suppress_technology_fee** | **bool** |  | [optional] 
**override_technology_fee** | **float** |  | [optional] 
**is_pf_lite** | **bool** |  | [optional] 
**is_pay_in_full** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_response import PaymentLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponse from a JSON string
payment_link_response_instance = PaymentLinkResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponse.to_json())

# convert the object into a dict
payment_link_response_dict = payment_link_response_instance.to_dict()
# create an instance of PaymentLinkResponse from a dict
payment_link_response_from_dict = PaymentLinkResponse.from_dict(payment_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


