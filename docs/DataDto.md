# DataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_number** | **int** |  | [optional] 
**memo** | **str** |  | [optional] 
**check_date** | **str** |  | [optional] 
**remittance_data** | [**RemittanceDataDto**](RemittanceDataDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.data_dto import DataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DataDto from a JSON string
data_dto_instance = DataDto.from_json(json)
# print the JSON string representation of the object
print(DataDto.to_json())

# convert the object into a dict
data_dto_dict = data_dto_instance.to_dict()
# create an instance of DataDto from a dict
data_dto_from_dict = DataDto.from_dict(data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


