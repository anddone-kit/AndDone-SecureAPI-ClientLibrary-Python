# VendorRequestDTORemittanceAddress

Required if `useSameAsPhysicalAddress` is false or missing. 

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
from openapi_client.models.vendor_request_dto_remittance_address import VendorRequestDTORemittanceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequestDTORemittanceAddress from a JSON string
vendor_request_dto_remittance_address_instance = VendorRequestDTORemittanceAddress.from_json(json)
# print the JSON string representation of the object
print(VendorRequestDTORemittanceAddress.to_json())

# convert the object into a dict
vendor_request_dto_remittance_address_dict = vendor_request_dto_remittance_address_instance.to_dict()
# create an instance of VendorRequestDTORemittanceAddress from a dict
vendor_request_dto_remittance_address_from_dict = VendorRequestDTORemittanceAddress.from_dict(vendor_request_dto_remittance_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


