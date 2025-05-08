# VendorRequestDTOPhysicalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** |  | 
**address_line1** | **str** |  | 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 
**postal_code** | **str** |  | 
**address_source** | **str** |  | 

## Example

```python
from openapi_client.models.vendor_request_dto_physical_address import VendorRequestDTOPhysicalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequestDTOPhysicalAddress from a JSON string
vendor_request_dto_physical_address_instance = VendorRequestDTOPhysicalAddress.from_json(json)
# print the JSON string representation of the object
print(VendorRequestDTOPhysicalAddress.to_json())

# convert the object into a dict
vendor_request_dto_physical_address_dict = vendor_request_dto_physical_address_instance.to_dict()
# create an instance of VendorRequestDTOPhysicalAddress from a dict
vendor_request_dto_physical_address_from_dict = VendorRequestDTOPhysicalAddress.from_dict(vendor_request_dto_physical_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


