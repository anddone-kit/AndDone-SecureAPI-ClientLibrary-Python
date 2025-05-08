# TransactionPaymentResponseBillingContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**TransactionPaymentResponseBillingContactName**](TransactionPaymentResponseBillingContactName.md) |  | [optional] 
**company_name** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**alternate_phone** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**address** | [**TransactionPaymentResponseBillingContactAddress**](TransactionPaymentResponseBillingContactAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_billing_contact import TransactionPaymentResponseBillingContact

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseBillingContact from a JSON string
transaction_payment_response_billing_contact_instance = TransactionPaymentResponseBillingContact.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseBillingContact.to_json())

# convert the object into a dict
transaction_payment_response_billing_contact_dict = transaction_payment_response_billing_contact_instance.to_dict()
# create an instance of TransactionPaymentResponseBillingContact from a dict
transaction_payment_response_billing_contact_from_dict = TransactionPaymentResponseBillingContact.from_dict(transaction_payment_response_billing_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


