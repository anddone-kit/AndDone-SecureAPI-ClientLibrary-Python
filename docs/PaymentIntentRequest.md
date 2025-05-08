# PaymentIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**amount** | **float** |  | 
**invoice_number** | **str** |  | [optional] 
**expires_in** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**payment_description** | **str** |  | [optional] 
**merchant_token** | **str** |  | [optional] 
**intent** | [**PaymentIntentRequestIntent**](PaymentIntentRequestIntent.md) |  | 
**save_for_future** | **bool** |  | [optional] 
**enable_premium_finance** | **bool** |  | [optional] 
**splits** | [**List[PaymentIntentRequestSplitsInner]**](PaymentIntentRequestSplitsInner.md) |  | [optional] 
**quote_key** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**suppress_technology_fee** | **bool** |  | [optional] 
**override_technology_fee** | **float** |  | [optional] 
**is_premium_financier** | **bool** |  | [optional] 
**pfr** | [**PaymentIntentRequestPfr**](PaymentIntentRequestPfr.md) |  | [optional] 
**save_customer** | **bool** |  | [optional] 
**customers** | [**List[PaymentIntentRequestCustomersInner]**](PaymentIntentRequestCustomersInner.md) |  | [optional] 
**additional_details_preference** | **str** |  | 
**selected_customer_fields** | **str** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reference_key** | **str** |  | [optional] 
**reference_data_list** | [**List[PaymentIntentRequestReferenceDataListInner]**](PaymentIntentRequestReferenceDataListInner.md) |  | [optional] 
**display_mode** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_intent_request import PaymentIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentRequest from a JSON string
payment_intent_request_instance = PaymentIntentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentRequest.to_json())

# convert the object into a dict
payment_intent_request_dict = payment_intent_request_instance.to_dict()
# create an instance of PaymentIntentRequest from a dict
payment_intent_request_from_dict = PaymentIntentRequest.from_dict(payment_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


