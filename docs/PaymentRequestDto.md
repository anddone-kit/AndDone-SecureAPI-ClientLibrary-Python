# PaymentRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | 
**payment_method** | **str** |  | 
**amount** | **float** |  | 
**bank_detail** | [**BankDetailDto**](BankDetailDto.md) |  | [optional] 
**data** | [**PaymentRequestDtoData**](PaymentRequestDtoData.md) |  | 

## Example

```python
from openapi_client.models.payment_request_dto import PaymentRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestDto from a JSON string
payment_request_dto_instance = PaymentRequestDto.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestDto.to_json())

# convert the object into a dict
payment_request_dto_dict = payment_request_dto_instance.to_dict()
# create an instance of PaymentRequestDto from a dict
payment_request_dto_from_dict = PaymentRequestDto.from_dict(payment_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


