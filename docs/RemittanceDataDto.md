# RemittanceDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headings** | [**List[HeadingDto]**](HeadingDto.md) |  | [optional] 
**rows** | **List[List[RowDto]]** |  | [optional] 

## Example

```python
from openapi_client.models.remittance_data_dto import RemittanceDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemittanceDataDto from a JSON string
remittance_data_dto_instance = RemittanceDataDto.from_json(json)
# print the JSON string representation of the object
print(RemittanceDataDto.to_json())

# convert the object into a dict
remittance_data_dto_dict = remittance_data_dto_instance.to_dict()
# create an instance of RemittanceDataDto from a dict
remittance_data_dto_from_dict = RemittanceDataDto.from_dict(remittance_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


