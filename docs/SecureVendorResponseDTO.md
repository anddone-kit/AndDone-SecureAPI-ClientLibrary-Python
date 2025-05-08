# SecureVendorResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_based_id** | **str** |  | [optional] 
**legal_entity_type** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**vendor_alias_name** | **str** |  | [optional] 
**vendor_db_name** | **str** |  | [optional] 
**payment_method_type** | **str** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**vendor_notes** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**is_mobile_number** | **bool** |  | [optional] 
**use_same_as_physical_address** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**remittance_address** | [**SecureVendorResponseDTORemittanceAddress**](SecureVendorResponseDTORemittanceAddress.md) |  | [optional] 
**physical_address** | [**SecureVendorResponseDTORemittanceAddress**](SecureVendorResponseDTORemittanceAddress.md) |  | [optional] 
**vendor_status** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.secure_vendor_response_dto import SecureVendorResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVendorResponseDTO from a JSON string
secure_vendor_response_dto_instance = SecureVendorResponseDTO.from_json(json)
# print the JSON string representation of the object
print(SecureVendorResponseDTO.to_json())

# convert the object into a dict
secure_vendor_response_dto_dict = secure_vendor_response_dto_instance.to_dict()
# create an instance of SecureVendorResponseDTO from a dict
secure_vendor_response_dto_from_dict = SecureVendorResponseDTO.from_dict(secure_vendor_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


