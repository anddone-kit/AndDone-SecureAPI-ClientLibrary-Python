# VendorResponseDTOTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_json** | **str** |  | [optional] 
**is_system_default** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.vendor_response_dto_template import VendorResponseDTOTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of VendorResponseDTOTemplate from a JSON string
vendor_response_dto_template_instance = VendorResponseDTOTemplate.from_json(json)
# print the JSON string representation of the object
print(VendorResponseDTOTemplate.to_json())

# convert the object into a dict
vendor_response_dto_template_dict = vendor_response_dto_template_instance.to_dict()
# create an instance of VendorResponseDTOTemplate from a dict
vendor_response_dto_template_from_dict = VendorResponseDTOTemplate.from_dict(vendor_response_dto_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


