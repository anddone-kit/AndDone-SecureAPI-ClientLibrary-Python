# PaymentIntentRequestPfr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_intent_request_pfr import PaymentIntentRequestPfr

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentRequestPfr from a JSON string
payment_intent_request_pfr_instance = PaymentIntentRequestPfr.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentRequestPfr.to_json())

# convert the object into a dict
payment_intent_request_pfr_dict = payment_intent_request_pfr_instance.to_dict()
# create an instance of PaymentIntentRequestPfr from a dict
payment_intent_request_pfr_from_dict = PaymentIntentRequestPfr.from_dict(payment_intent_request_pfr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


