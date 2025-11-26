# PaymentDetailResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**merchant_dba_name** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**check_number** | **int** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_account_number** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 
**payment_method_status** | **str** |  | [optional] 
**remittance_data** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_detail_response_dto import PaymentDetailResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailResponseDTO from a JSON string
payment_detail_response_dto_instance = PaymentDetailResponseDTO.from_json(json)
# print the JSON string representation of the object
print(PaymentDetailResponseDTO.to_json())

# convert the object into a dict
payment_detail_response_dto_dict = payment_detail_response_dto_instance.to_dict()
# create an instance of PaymentDetailResponseDTO from a dict
payment_detail_response_dto_from_dict = PaymentDetailResponseDTO.from_dict(payment_detail_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


