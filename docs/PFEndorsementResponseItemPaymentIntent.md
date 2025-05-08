# PFEndorsementResponseItemPaymentIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_token** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**expire_on** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**payment_description** | **str** |  | [optional] 
**intent** | [**PFEndorsementResponseItemPaymentIntentIntent**](PFEndorsementResponseItemPaymentIntentIntent.md) |  | [optional] 

## Example

```python
from openapi_client.models.pf_endorsement_response_item_payment_intent import PFEndorsementResponseItemPaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of PFEndorsementResponseItemPaymentIntent from a JSON string
pf_endorsement_response_item_payment_intent_instance = PFEndorsementResponseItemPaymentIntent.from_json(json)
# print the JSON string representation of the object
print(PFEndorsementResponseItemPaymentIntent.to_json())

# convert the object into a dict
pf_endorsement_response_item_payment_intent_dict = pf_endorsement_response_item_payment_intent_instance.to_dict()
# create an instance of PFEndorsementResponseItemPaymentIntent from a dict
pf_endorsement_response_item_payment_intent_from_dict = PFEndorsementResponseItemPaymentIntent.from_dict(pf_endorsement_response_item_payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


