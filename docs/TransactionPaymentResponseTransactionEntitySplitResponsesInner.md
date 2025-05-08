# TransactionPaymentResponseTransactionEntitySplitResponsesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_alias** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**charge_indicator** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_transaction_entity_split_responses_inner import TransactionPaymentResponseTransactionEntitySplitResponsesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseTransactionEntitySplitResponsesInner from a JSON string
transaction_payment_response_transaction_entity_split_responses_inner_instance = TransactionPaymentResponseTransactionEntitySplitResponsesInner.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseTransactionEntitySplitResponsesInner.to_json())

# convert the object into a dict
transaction_payment_response_transaction_entity_split_responses_inner_dict = transaction_payment_response_transaction_entity_split_responses_inner_instance.to_dict()
# create an instance of TransactionPaymentResponseTransactionEntitySplitResponsesInner from a dict
transaction_payment_response_transaction_entity_split_responses_inner_from_dict = TransactionPaymentResponseTransactionEntitySplitResponsesInner.from_dict(transaction_payment_response_transaction_entity_split_responses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


