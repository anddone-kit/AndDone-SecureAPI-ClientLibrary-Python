# PageVendorResponseDTODataInner


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
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor_status** | **str** |  | [optional] 
**use_same_as_physical_address** | **bool** |  | [optional] 
**physical_address** | [**VendorResponseDTORemittanceAddress**](VendorResponseDTORemittanceAddress.md) |  | [optional] 
**remittance_address** | [**VendorResponseDTORemittanceAddress**](VendorResponseDTORemittanceAddress.md) |  | [optional] 
**verification_results** | [**VendorResponseDTOVerificationResultsInner**](VendorResponseDTOVerificationResultsInner.md) |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**approved_date** | **str** |  | [optional] 
**template** | [**VendorResponseDTOTemplate**](VendorResponseDTOTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.page_vendor_response_dto_data_inner import PageVendorResponseDTODataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PageVendorResponseDTODataInner from a JSON string
page_vendor_response_dto_data_inner_instance = PageVendorResponseDTODataInner.from_json(json)
# print the JSON string representation of the object
print(PageVendorResponseDTODataInner.to_json())

# convert the object into a dict
page_vendor_response_dto_data_inner_dict = page_vendor_response_dto_data_inner_instance.to_dict()
# create an instance of PageVendorResponseDTODataInner from a dict
page_vendor_response_dto_data_inner_from_dict = PageVendorResponseDTODataInner.from_dict(page_vendor_response_dto_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


