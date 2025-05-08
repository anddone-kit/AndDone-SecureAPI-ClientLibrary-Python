# TransactionPaymentResponseBillingContactName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_billing_contact_name import TransactionPaymentResponseBillingContactName

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseBillingContactName from a JSON string
transaction_payment_response_billing_contact_name_instance = TransactionPaymentResponseBillingContactName.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseBillingContactName.to_json())

# convert the object into a dict
transaction_payment_response_billing_contact_name_dict = transaction_payment_response_billing_contact_name_instance.to_dict()
# create an instance of TransactionPaymentResponseBillingContactName from a dict
transaction_payment_response_billing_contact_name_from_dict = TransactionPaymentResponseBillingContactName.from_dict(transaction_payment_response_billing_contact_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


