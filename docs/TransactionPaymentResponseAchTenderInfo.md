# TransactionPaymentResponseAchTenderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_name** | **str** |  | [optional] 
**routing_number** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**check_type** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**name_on_check** | **str** |  | [optional] 
**account_holder_name** | **str** |  | [optional] 
**account_category** | **str** |  | [optional] 
**capture_amount** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**convenience_amount** | **float** |  | [optional] 
**bin_number** | **str** |  | [optional] 
**adjustment_percent_value** | **float** |  | [optional] 
**adjustment_fixed_value** | **float** |  | [optional] 
**adjustment_amount** | **float** |  | [optional] 
**adjustment_display_name** | **str** |  | [optional] 
**adjustment_descriptor_message** | **str** |  | [optional] 
**payment_adjustment_type** | **str** |  | [optional] 
**pre_auth_code** | **str** |  | [optional] 
**mask_account** | **str** |  | [optional] 
**account_token** | **str** |  | [optional] 
**account_token_message** | **str** |  | [optional] 
**create_account_token** | **bool** |  | [optional] 
**commission_type** | [**TransactionPaymentResponseAchTenderInfoCommissionType**](TransactionPaymentResponseAchTenderInfoCommissionType.md) |  | [optional] 
**commission_value** | **float** |  | [optional] 
**commission_fixed_value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payment_response_ach_tender_info import TransactionPaymentResponseAchTenderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPaymentResponseAchTenderInfo from a JSON string
transaction_payment_response_ach_tender_info_instance = TransactionPaymentResponseAchTenderInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionPaymentResponseAchTenderInfo.to_json())

# convert the object into a dict
transaction_payment_response_ach_tender_info_dict = transaction_payment_response_ach_tender_info_instance.to_dict()
# create an instance of TransactionPaymentResponseAchTenderInfo from a dict
transaction_payment_response_ach_tender_info_from_dict = TransactionPaymentResponseAchTenderInfo.from_dict(transaction_payment_response_ach_tender_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


