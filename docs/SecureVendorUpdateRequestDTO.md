# SecureVendorUpdateRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | 
**vendor_name** | **str** |  | [optional] 
**vendor_alias_name** | **str** |  | [optional] 
**vendor_db_name** | **str** | Database name of the vendor | [optional] 
**legal_entity_type** | **str** |  | [optional] 
**payment_method_type** | **str** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**vendor_notes** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**is_mobile_number** | **bool** |  | [optional] 
**use_same_as_physical_address** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**remittance_address** | [**SecureVendorUpdateRequestDTORemittanceAddress**](SecureVendorUpdateRequestDTORemittanceAddress.md) |  | [optional] 
**physical_address** | [**SecureVendorUpdateRequestDTORemittanceAddress**](SecureVendorUpdateRequestDTORemittanceAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.secure_vendor_update_request_dto import SecureVendorUpdateRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVendorUpdateRequestDTO from a JSON string
secure_vendor_update_request_dto_instance = SecureVendorUpdateRequestDTO.from_json(json)
# print the JSON string representation of the object
print(SecureVendorUpdateRequestDTO.to_json())

# convert the object into a dict
secure_vendor_update_request_dto_dict = secure_vendor_update_request_dto_instance.to_dict()
# create an instance of SecureVendorUpdateRequestDTO from a dict
secure_vendor_update_request_dto_from_dict = SecureVendorUpdateRequestDTO.from_dict(secure_vendor_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


