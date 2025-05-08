# PageVendorResponseDTODataInnerVerificationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**verification_type** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**verification_reason** | **str** |  | [optional] 
**verified_on** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.page_vendor_response_dto_data_inner_verification_results import PageVendorResponseDTODataInnerVerificationResults

# TODO update the JSON string below
json = "{}"
# create an instance of PageVendorResponseDTODataInnerVerificationResults from a JSON string
page_vendor_response_dto_data_inner_verification_results_instance = PageVendorResponseDTODataInnerVerificationResults.from_json(json)
# print the JSON string representation of the object
print(PageVendorResponseDTODataInnerVerificationResults.to_json())

# convert the object into a dict
page_vendor_response_dto_data_inner_verification_results_dict = page_vendor_response_dto_data_inner_verification_results_instance.to_dict()
# create an instance of PageVendorResponseDTODataInnerVerificationResults from a dict
page_vendor_response_dto_data_inner_verification_results_from_dict = PageVendorResponseDTODataInnerVerificationResults.from_dict(page_vendor_response_dto_data_inner_verification_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


