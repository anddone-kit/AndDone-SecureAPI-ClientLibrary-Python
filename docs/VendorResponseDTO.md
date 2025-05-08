# VendorResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_based_id** | **str** |  | [optional] 
**legal_entity_type** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**vendor_alias_name** | **str** |  | [optional] 
**vendor_db_name** | **str** | Database name of the vendor | [optional] 
**payment_method_type** | **str** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**vendor_notes** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**is_mobile_number** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor_status** | **str** |  | [optional] 
**use_same_as_physical_address** | **bool** |  | [optional] 
**remittance_address** | [**VendorResponseDTORemittanceAddress**](VendorResponseDTORemittanceAddress.md) |  | [optional] 
**physical_address** | [**VendorResponseDTORemittanceAddress**](VendorResponseDTORemittanceAddress.md) |  | [optional] 
**verification_results** | [**List[VendorResponseDTOVerificationResultsInner]**](VendorResponseDTOVerificationResultsInner.md) |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**approved_date** | **str** |  | [optional] 
**template** | [**VendorResponseDTOTemplate**](VendorResponseDTOTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.vendor_response_dto import VendorResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VendorResponseDTO from a JSON string
vendor_response_dto_instance = VendorResponseDTO.from_json(json)
# print the JSON string representation of the object
print(VendorResponseDTO.to_json())

# convert the object into a dict
vendor_response_dto_dict = vendor_response_dto_instance.to_dict()
# create an instance of VendorResponseDTO from a dict
vendor_response_dto_from_dict = VendorResponseDTO.from_dict(vendor_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


