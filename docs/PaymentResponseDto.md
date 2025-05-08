# PaymentResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 
**payment_method_status** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**data** | [**DataDto**](DataDto.md) |  | [optional] 
**bank_account_details** | **str** | JSON-encoded string containing bank account details | [optional] 
**vendor_address** | **str** | JSON-encoded string containing vendor address | [optional] 

## Example

```python
from openapi_client.models.payment_response_dto import PaymentResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponseDto from a JSON string
payment_response_dto_instance = PaymentResponseDto.from_json(json)
# print the JSON string representation of the object
print(PaymentResponseDto.to_json())

# convert the object into a dict
payment_response_dto_dict = payment_response_dto_instance.to_dict()
# create an instance of PaymentResponseDto from a dict
payment_response_dto_from_dict = PaymentResponseDto.from_dict(payment_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


