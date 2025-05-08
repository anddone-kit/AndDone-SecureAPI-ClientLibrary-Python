# PaymentLinkResponseCustomersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**notify_via_sms** | **bool** |  | [optional] 
**notify_via_email** | **bool** |  | [optional] 
**created_on** | **str** |  | [optional] 
**accounts** | [**List[PaymentLinkResponseCustomersInnerAccountsInner]**](PaymentLinkResponseCustomersInnerAccountsInner.md) |  | [optional] 
**address** | [**TransactionPaymentResponseBillingContactAddress**](TransactionPaymentResponseBillingContactAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_response_customers_inner import PaymentLinkResponseCustomersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponseCustomersInner from a JSON string
payment_link_response_customers_inner_instance = PaymentLinkResponseCustomersInner.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponseCustomersInner.to_json())

# convert the object into a dict
payment_link_response_customers_inner_dict = payment_link_response_customers_inner_instance.to_dict()
# create an instance of PaymentLinkResponseCustomersInner from a dict
payment_link_response_customers_inner_from_dict = PaymentLinkResponseCustomersInner.from_dict(payment_link_response_customers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


