# PaymentLinkResponsePaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**transaction_status** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**auth_code** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**account_token** | **str** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**masked_account** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_response_payments_inner import PaymentLinkResponsePaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponsePaymentsInner from a JSON string
payment_link_response_payments_inner_instance = PaymentLinkResponsePaymentsInner.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponsePaymentsInner.to_json())

# convert the object into a dict
payment_link_response_payments_inner_dict = payment_link_response_payments_inner_instance.to_dict()
# create an instance of PaymentLinkResponsePaymentsInner from a dict
payment_link_response_payments_inner_from_dict = PaymentLinkResponsePaymentsInner.from_dict(payment_link_response_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


