# TransactionPaymentResponseRefundTransactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_row_count** | **int** |  | [optional] 
**data** | [**List[TransactionPaymentResponseRefundTransactionsDataInner]**](TransactionPaymentResponseRefundTransactionsDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_refund_transactions import TransactionPaymentResponseRefundTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseRefundTransactions from a JSON string
transaction_payment_response_refund_transactions_instance = TransactionPaymentResponseRefundTransactions.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseRefundTransactions.to_json())

# convert the object into a dict
transaction_payment_response_refund_transactions_dict = transaction_payment_response_refund_transactions_instance.to_dict()
# create an instance of TransactionPaymentResponseRefundTransactions from a dict
transaction_payment_response_refund_transactions_from_dict = TransactionPaymentResponseRefundTransactions.from_dict(transaction_payment_response_refund_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


