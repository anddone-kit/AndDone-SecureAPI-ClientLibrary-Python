# PaymentIntentRequestCustomersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_intent_request_customers_inner import PaymentIntentRequestCustomersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentRequestCustomersInner from a JSON string
payment_intent_request_customers_inner_instance = PaymentIntentRequestCustomersInner.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentRequestCustomersInner.to_json())

# convert the object into a dict
payment_intent_request_customers_inner_dict = payment_intent_request_customers_inner_instance.to_dict()
# create an instance of PaymentIntentRequestCustomersInner from a dict
payment_intent_request_customers_inner_from_dict = PaymentIntentRequestCustomersInner.from_dict(payment_intent_request_customers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


