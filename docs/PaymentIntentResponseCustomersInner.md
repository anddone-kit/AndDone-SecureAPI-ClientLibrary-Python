# PaymentIntentResponseCustomersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_intent_response_customers_inner import PaymentIntentResponseCustomersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentResponseCustomersInner from a JSON string
payment_intent_response_customers_inner_instance = PaymentIntentResponseCustomersInner.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentResponseCustomersInner.to_json())

# convert the object into a dict
payment_intent_response_customers_inner_dict = payment_intent_response_customers_inner_instance.to_dict()
# create an instance of PaymentIntentResponseCustomersInner from a dict
payment_intent_response_customers_inner_from_dict = PaymentIntentResponseCustomersInner.from_dict(payment_intent_response_customers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


