# VendorRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** |  | 
**vendor_alias_name** | **str** |  | [optional] 
**vendor_db_name** | **str** | Database name of the vendor | 
**legal_entity_type** | **str** |  | 
**payment_method_type** | **str** |  | 
**notification_type** | **str** |  | 
**vendor_notes** | **str** |  | [optional] 
**phone_number** | **str** |  | 
**is_mobile_number** | **bool** |  | [optional] 
**use_same_as_physical_address** | **bool** |  | [optional] 
**email** | **str** |  | 
**url** | **str** |  | [optional] 
**remittance_address** | [**VendorRequestDTORemittanceAddress**](VendorRequestDTORemittanceAddress.md) |  | [optional] 
**physical_address** | [**VendorRequestDTOPhysicalAddress**](VendorRequestDTOPhysicalAddress.md) |  | 

## Example

```python
from openapi_client.models.vendor_request_dto import VendorRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequestDTO from a JSON string
vendor_request_dto_instance = VendorRequestDTO.from_json(json)
# print the JSON string representation of the object
print(VendorRequestDTO.to_json())

# convert the object into a dict
vendor_request_dto_dict = vendor_request_dto_instance.to_dict()
# create an instance of VendorRequestDTO from a dict
vendor_request_dto_from_dict = VendorRequestDTO.from_dict(vendor_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


