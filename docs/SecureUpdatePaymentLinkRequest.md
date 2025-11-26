# SecureUpdatePaymentLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**payment_description** | **str** |  | [optional] 
**customers** | [**List[PaymentLinkResponseCustomersInner]**](PaymentLinkResponseCustomersInner.md) |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**expire_by** | **int** |  | [optional] 
**expire_on** | **str** |  | [optional] 
**line_items** | [**List[PaymentLinkResponseLineItemsInner]**](PaymentLinkResponseLineItemsInner.md) |  | [optional] 
**short_description** | **str** |  | [optional] 
**response_type** | **str** |  | [optional] 
**callback_parameters** | [**PaymentLinkResponseCallbackParameters**](PaymentLinkResponseCallbackParameters.md) |  | [optional] 
**payment_link_type** | **str** |  | [optional] 
**save_for_future** | **bool** |  | [optional] 
**splits** | [**List[PaymentIntentRequestSplitsInner]**](PaymentIntentRequestSplitsInner.md) |  | [optional] 
**quote_key** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reference_key** | **str** |  | [optional] 
**reference_data_list** | [**List[PaymentLinkResponseReferenceDataListInner]**](PaymentLinkResponseReferenceDataListInner.md) |  | [optional] 
**platform_settlement_status** | **str** |  | [optional] 
**is_pay_in_full** | **bool** |  | [optional] 
**is_premium_financier** | **bool** |  | [optional] 
**pfr** | [**PaymentIntentRequestPfr**](PaymentIntentRequestPfr.md) |  | [optional] 
**pf_type** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**enable_premium_finance** | **bool** |  | [optional] 
**expire_in** | **int** |  | [optional] 
**expire_in_unit** | **str** |  | [optional] 
**settings** | [**SecureUpdatePaymentLinkRequestSettings**](SecureUpdatePaymentLinkRequestSettings.md) |  | [optional] 
**suppress_technology_fee** | **bool** |  | [optional] 
**override_technology_fee** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.secure_update_payment_link_request import SecureUpdatePaymentLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecureUpdatePaymentLinkRequest from a JSON string
secure_update_payment_link_request_instance = SecureUpdatePaymentLinkRequest.from_json(json)
# print the JSON string representation of the object
print(SecureUpdatePaymentLinkRequest.to_json())

# convert the object into a dict
secure_update_payment_link_request_dict = secure_update_payment_link_request_instance.to_dict()
# create an instance of SecureUpdatePaymentLinkRequest from a dict
secure_update_payment_link_request_from_dict = SecureUpdatePaymentLinkRequest.from_dict(secure_update_payment_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


