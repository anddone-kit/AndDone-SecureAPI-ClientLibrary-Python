# RowDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.row_dto import RowDto

# TODO update the JSON string below
json = "{}"
# create an instance of RowDto from a JSON string
row_dto_instance = RowDto.from_json(json)
# print the JSON string representation of the object
print(RowDto.to_json())

# convert the object into a dict
row_dto_dict = row_dto_instance.to_dict()
# create an instance of RowDto from a dict
row_dto_from_dict = RowDto.from_dict(row_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


