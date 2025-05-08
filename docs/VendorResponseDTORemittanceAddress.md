# VendorResponseDTORemittanceAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**attention** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**address_type** | **str** |  | [optional] 
**address_source** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.vendor_response_dto_remittance_address import VendorResponseDTORemittanceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of VendorResponseDTORemittanceAddress from a JSON string
vendor_response_dto_remittance_address_instance = VendorResponseDTORemittanceAddress.from_json(json)
# print the JSON string representation of the object
print(VendorResponseDTORemittanceAddress.to_json())

# convert the object into a dict
vendor_response_dto_remittance_address_dict = vendor_response_dto_remittance_address_instance.to_dict()
# create an instance of VendorResponseDTORemittanceAddress from a dict
vendor_response_dto_remittance_address_from_dict = VendorResponseDTORemittanceAddress.from_dict(vendor_response_dto_remittance_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


