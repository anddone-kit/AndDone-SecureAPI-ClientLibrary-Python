# BankDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**routing_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_detail_dto import BankDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankDetailDto from a JSON string
bank_detail_dto_instance = BankDetailDto.from_json(json)
# print the JSON string representation of the object
print(BankDetailDto.to_json())

# convert the object into a dict
bank_detail_dto_dict = bank_detail_dto_instance.to_dict()
# create an instance of BankDetailDto from a dict
bank_detail_dto_from_dict = BankDetailDto.from_dict(bank_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


