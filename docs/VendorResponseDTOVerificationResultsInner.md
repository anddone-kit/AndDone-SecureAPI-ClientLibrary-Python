# VendorResponseDTOVerificationResultsInner


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
from openapi_client.models.vendor_response_dto_verification_results_inner import VendorResponseDTOVerificationResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorResponseDTOVerificationResultsInner from a JSON string
vendor_response_dto_verification_results_inner_instance = VendorResponseDTOVerificationResultsInner.from_json(json)
# print the JSON string representation of the object
print(VendorResponseDTOVerificationResultsInner.to_json())

# convert the object into a dict
vendor_response_dto_verification_results_inner_dict = vendor_response_dto_verification_results_inner_instance.to_dict()
# create an instance of VendorResponseDTOVerificationResultsInner from a dict
vendor_response_dto_verification_results_inner_from_dict = VendorResponseDTOVerificationResultsInner.from_dict(vendor_response_dto_verification_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


