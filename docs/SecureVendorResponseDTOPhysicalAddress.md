# SecureVendorResponseDTOPhysicalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** | Attention to (optional) | [optional] 
**address_line1** | **str** | Address line 1 | [optional] 
**address_line2** | **str** | Address line 2 (optional) | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Country | [optional] 
**postal_code** | **str** | Postal code | [optional] 
**address_type** | **str** |  | [optional] 
**address_source** | **str** |  | [optional] 
**vendor_status** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**approved_date** | **str** |  | [optional] 
**ofac_verified** | **str** |  | [optional] 
**address_verified** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.secure_vendor_response_dto_physical_address import SecureVendorResponseDTOPhysicalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVendorResponseDTOPhysicalAddress from a JSON string
secure_vendor_response_dto_physical_address_instance = SecureVendorResponseDTOPhysicalAddress.from_json(json)
# print the JSON string representation of the object
print(SecureVendorResponseDTOPhysicalAddress.to_json())

# convert the object into a dict
secure_vendor_response_dto_physical_address_dict = secure_vendor_response_dto_physical_address_instance.to_dict()
# create an instance of SecureVendorResponseDTOPhysicalAddress from a dict
secure_vendor_response_dto_physical_address_from_dict = SecureVendorResponseDTOPhysicalAddress.from_dict(secure_vendor_response_dto_physical_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


