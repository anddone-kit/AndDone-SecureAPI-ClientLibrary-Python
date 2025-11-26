# HeadingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**is_aggregate_amount** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.heading_dto import HeadingDto

# TODO update the JSON string below
json = "{}"
# create an instance of HeadingDto from a JSON string
heading_dto_instance = HeadingDto.from_json(json)
# print the JSON string representation of the object
print(HeadingDto.to_json())

# convert the object into a dict
heading_dto_dict = heading_dto_instance.to_dict()
# create an instance of HeadingDto from a dict
heading_dto_from_dict = HeadingDto.from_dict(heading_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


