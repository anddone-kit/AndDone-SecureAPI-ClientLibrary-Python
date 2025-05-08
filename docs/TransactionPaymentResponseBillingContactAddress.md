# TransactionPaymentResponseBillingContactAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **int** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_billing_contact_address import TransactionPaymentResponseBillingContactAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseBillingContactAddress from a JSON string
transaction_payment_response_billing_contact_address_instance = TransactionPaymentResponseBillingContactAddress.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseBillingContactAddress.to_json())

# convert the object into a dict
transaction_payment_response_billing_contact_address_dict = transaction_payment_response_billing_contact_address_instance.to_dict()
# create an instance of TransactionPaymentResponseBillingContactAddress from a dict
transaction_payment_response_billing_contact_address_from_dict = TransactionPaymentResponseBillingContactAddress.from_dict(transaction_payment_response_billing_contact_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


