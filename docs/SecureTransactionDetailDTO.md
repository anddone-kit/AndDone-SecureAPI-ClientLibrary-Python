# SecureTransactionDetailDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**trace_number** | **str** |  | [optional] 
**transaction_code** | **str** |  | [optional] 
**transaction_origin** | **str** |  | [optional] 
**refund_origin** | [**TransactionPaymentResponseRefundOrigin**](TransactionPaymentResponseRefundOrigin.md) |  | [optional] 
**billing_contact** | [**TransactionPaymentResponseBillingContact**](TransactionPaymentResponseBillingContact.md) |  | [optional] 
**shipping_contact** | [**TransactionPaymentResponseBillingContact**](TransactionPaymentResponseBillingContact.md) |  | [optional] 
**reference_transaction_id** | **str** |  | [optional] 
**transaction_date** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**operation_type** | **str** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**process_method** | **str** |  | [optional] 
**processor_name** | **str** |  | [optional] 
**is_debit** | **bool** |  | [optional] 
**tender_info** | [**SecureTransactionDetailDTOTenderInfo**](SecureTransactionDetailDTOTenderInfo.md) |  | [optional] 
**reference_customer_id** | **str** |  | [optional] 
**invoice_no** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**recurring_type** | **str** |  | [optional] 
**recurring_id** | **str** |  | [optional] 
**installment_number** | **float** |  | [optional] 
**installment_count** | **float** |  | [optional] 
**allow_duplicates** | **bool** |  | [optional] 
**verification_enabled** | **bool** |  | [optional] 
**sent_success_notification** | **bool** |  | [optional] 
**sent_failed_notification** | **bool** |  | [optional] 
**training_mode** | **bool** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**is_offline** | **bool** |  | [optional] 
**transaction_status** | **str** |  | [optional] 
**previous_transaction_status** | **str** |  | [optional] 
**transaction_result** | [**TransactionPaymentResponseTransactionResult**](TransactionPaymentResponseTransactionResult.md) |  | [optional] 
**level** | **float** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**payment_link_id** | **str** |  | [optional] 
**additional_fields** | **str** |  | [optional] 
**settlement_date** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**payment_reference** | **str** |  | [optional] 
**refund_reference** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.secure_transaction_detail_dto import SecureTransactionDetailDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecureTransactionDetailDTO from a JSON string
secure_transaction_detail_dto_instance = SecureTransactionDetailDTO.from_json(json)
# print the JSON string representation of the object
print(SecureTransactionDetailDTO.to_json())

# convert the object into a dict
secure_transaction_detail_dto_dict = secure_transaction_detail_dto_instance.to_dict()
# create an instance of SecureTransactionDetailDTO from a dict
secure_transaction_detail_dto_from_dict = SecureTransactionDetailDTO.from_dict(secure_transaction_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


