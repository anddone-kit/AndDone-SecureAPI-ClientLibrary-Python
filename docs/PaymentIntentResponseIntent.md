# PaymentIntentResponseIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_types** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.payment_intent_response_intent import PaymentIntentResponseIntent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentResponseIntent from a JSON string
payment_intent_response_intent_instance = PaymentIntentResponseIntent.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentResponseIntent.to_json())

# convert the object into a dict
payment_intent_response_intent_dict = payment_intent_response_intent_instance.to_dict()
# create an instance of PaymentIntentResponseIntent from a dict
payment_intent_response_intent_from_dict = PaymentIntentResponseIntent.from_dict(payment_intent_response_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


