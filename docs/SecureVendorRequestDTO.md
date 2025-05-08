# SecureVendorRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | 

## Example

```python
from openapi_client.models.secure_vendor_request_dto import SecureVendorRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVendorRequestDTO from a JSON string
secure_vendor_request_dto_instance = SecureVendorRequestDTO.from_json(json)
# print the JSON string representation of the object
print(SecureVendorRequestDTO.to_json())

# convert the object into a dict
secure_vendor_request_dto_dict = secure_vendor_request_dto_instance.to_dict()
# create an instance of SecureVendorRequestDTO from a dict
secure_vendor_request_dto_from_dict = SecureVendorRequestDTO.from_dict(secure_vendor_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


