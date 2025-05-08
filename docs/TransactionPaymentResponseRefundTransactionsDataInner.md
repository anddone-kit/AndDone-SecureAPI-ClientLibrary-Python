# TransactionPaymentResponseRefundTransactionsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**transaction_date** | **str** |  | [optional] 
**operation_type** | **str** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**process_method** | **str** |  | [optional] 
**is_debit** | **bool** |  | [optional] 
**reference_transaction_id** | **str** |  | [optional] 
**reference_customer_id** | **str** |  | [optional] 
**recurring_id** | **str** |  | [optional] 
**batch_id** | **str** |  | [optional] 
**transaction_status** | **str** |  | [optional] 
**settlement_date** | **str** |  | [optional] 
**auth_code** | **str** |  | [optional] 
**card_number** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**bin_number** | **str** |  | [optional] 
**cheque_number** | **str** |  | [optional] 
**routing_number** | **str** |  | [optional] 
**name_on_check_or_card** | **str** |  | [optional] 
**account_holder_name** | **str** |  | [optional] 
**account_category** | **str** |  | [optional] 
**training_mode** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**convenience_amount** | **float** |  | [optional] 
**capture_amount** | **float** |  | [optional] 
**card_type** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**partner_name** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**payment_link_id** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**processor_name** | **str** |  | [optional] 
**processor_display_name** | **str** |  | [optional] 
**verification2_code** | **str** |  | [optional] 
**transaction_origin** | **str** |  | [optional] 
**previous_transaction_status** | **str** |  | [optional] 
**trace_number** | **str** |  | [optional] 
**merchant_reference** | **str** |  | [optional] 
**additiona_fields** | **str** |  | [optional] 
**adjustment_value** | **float** |  | [optional] 
**adjustment_fixed_value** | **float** |  | [optional] 
**adjustment_amount** | **float** |  | [optional] 
**adjustment_display_name** | **str** |  | [optional] 
**adjustment_descriptor_message** | **str** |  | [optional] 
**payment_adjustment_type** | **str** |  | [optional] 
**commission_type** | [**TransactionPaymentResponseAchTenderInfoCommissionType**](TransactionPaymentResponseAchTenderInfoCommissionType.md) |  | [optional] 
**commission_value** | **float** |  | [optional] 
**commission_fixed_value** | **float** |  | [optional] 
**account_token** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**payment_category** | **str** |  | [optional] 
**refund_reason** | **str** |  | [optional] 
**refund_detail** | **str** |  | [optional] 
**full_account_number** | **str** |  | [optional] 
**refund_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_refund_transactions_data_inner import TransactionPaymentResponseRefundTransactionsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseRefundTransactionsDataInner from a JSON string
transaction_payment_response_refund_transactions_data_inner_instance = TransactionPaymentResponseRefundTransactionsDataInner.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseRefundTransactionsDataInner.to_json())

# convert the object into a dict
transaction_payment_response_refund_transactions_data_inner_dict = transaction_payment_response_refund_transactions_data_inner_instance.to_dict()
# create an instance of TransactionPaymentResponseRefundTransactionsDataInner from a dict
transaction_payment_response_refund_transactions_data_inner_from_dict = TransactionPaymentResponseRefundTransactionsDataInner.from_dict(transaction_payment_response_refund_transactions_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


