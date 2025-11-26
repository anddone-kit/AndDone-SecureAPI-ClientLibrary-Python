# AutoPayEnrollmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**is_success** | **bool** |  | [optional] 
**integration_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auto_pay_enrollment_response import AutoPayEnrollmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoPayEnrollmentResponse from a JSON string
auto_pay_enrollment_response_instance = AutoPayEnrollmentResponse.from_json(json)
# print the JSON string representation of the object
print(AutoPayEnrollmentResponse.to_json())

# convert the object into a dict
auto_pay_enrollment_response_dict = auto_pay_enrollment_response_instance.to_dict()
# create an instance of AutoPayEnrollmentResponse from a dict
auto_pay_enrollment_response_from_dict = AutoPayEnrollmentResponse.from_dict(auto_pay_enrollment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


