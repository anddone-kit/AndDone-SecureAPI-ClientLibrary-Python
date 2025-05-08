# SecureVendorStatusRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from openapi_client.models.secure_vendor_status_request_dto import SecureVendorStatusRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVendorStatusRequestDTO from a JSON string
secure_vendor_status_request_dto_instance = SecureVendorStatusRequestDTO.from_json(json)
# print the JSON string representation of the object
print(SecureVendorStatusRequestDTO.to_json())

# convert the object into a dict
secure_vendor_status_request_dto_dict = secure_vendor_status_request_dto_instance.to_dict()
# create an instance of SecureVendorStatusRequestDTO from a dict
secure_vendor_status_request_dto_from_dict = SecureVendorStatusRequestDTO.from_dict(secure_vendor_status_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


