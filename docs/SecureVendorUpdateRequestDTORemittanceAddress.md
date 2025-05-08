# SecureVendorUpdateRequestDTORemittanceAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**address_source** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.secure_vendor_update_request_dto_remittance_address import SecureVendorUpdateRequestDTORemittanceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVendorUpdateRequestDTORemittanceAddress from a JSON string
secure_vendor_update_request_dto_remittance_address_instance = SecureVendorUpdateRequestDTORemittanceAddress.from_json(json)
# print the JSON string representation of the object
print(SecureVendorUpdateRequestDTORemittanceAddress.to_json())

# convert the object into a dict
secure_vendor_update_request_dto_remittance_address_dict = secure_vendor_update_request_dto_remittance_address_instance.to_dict()
# create an instance of SecureVendorUpdateRequestDTORemittanceAddress from a dict
secure_vendor_update_request_dto_remittance_address_from_dict = SecureVendorUpdateRequestDTORemittanceAddress.from_dict(secure_vendor_update_request_dto_remittance_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


