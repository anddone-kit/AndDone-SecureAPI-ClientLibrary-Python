# TransactionPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**transaction_code** | **str** |  | [optional] 
**billing_contact** | [**TransactionPaymentResponseBillingContact**](TransactionPaymentResponseBillingContact.md) |  | [optional] 
**transaction_date** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**process_method** | **str** |  | [optional] 
**processor_name** | **str** |  | [optional] 
**transaction_origin** | **str** |  | [optional] 
**refund_origin** | [**TransactionPaymentResponseRefundOrigin**](TransactionPaymentResponseRefundOrigin.md) |  | [optional] 
**ach_tender_info** | [**TransactionPaymentResponseAchTenderInfo**](TransactionPaymentResponseAchTenderInfo.md) |  | [optional] 
**cc_tender_info** | [**TransactionPaymentResponseCcTenderInfo**](TransactionPaymentResponseCcTenderInfo.md) |  | [optional] 
**debit_card_tender_info** | [**TransactionPaymentResponseCcTenderInfo**](TransactionPaymentResponseCcTenderInfo.md) |  | [optional] 
**reference_customer_id** | **str** |  | [optional] 
**invoice_no** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**transaction_status** | **str** |  | [optional] 
**transaction_result** | [**TransactionPaymentResponseTransactionResult**](TransactionPaymentResponseTransactionResult.md) |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**payment_link_id** | **str** |  | [optional] 
**additional_fields** | **str** |  | [optional] 
**settlement_date** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**payment_category** | **str** |  | [optional] 
**transaction_entity_split_responses** | [**List[TransactionPaymentResponseTransactionEntitySplitResponsesInner]**](TransactionPaymentResponseTransactionEntitySplitResponsesInner.md) |  | [optional] 
**payment_description** | **str** |  | [optional] 
**refund_transactions** | [**TransactionPaymentResponseRefundTransactions**](TransactionPaymentResponseRefundTransactions.md) |  | [optional] 
**chargeback_target_account** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**charge_back_amount** | **float** |  | [optional] 
**suppress_technology_fee** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response import TransactionPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponse from a JSON string
transaction_payment_response_instance = TransactionPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponse.to_json())

# convert the object into a dict
transaction_payment_response_dict = transaction_payment_response_instance.to_dict()
# create an instance of TransactionPaymentResponse from a dict
transaction_payment_response_from_dict = TransactionPaymentResponse.from_dict(transaction_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


