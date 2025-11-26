# AutoPayEnrollmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | [optional] 
**quote_key** | **str** |  | 
**payment_intent_id** | **str** |  | 
**email_address** | **str** |  | 
**process_method** | **str** |  | 
**credit_card_token** | **str** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**cardholder_name** | **str** |  | [optional] 
**adyen_psp** | **str** |  | [optional] 
**account_owner_name** | **str** |  | [optional] 
**bank_routing_number** | **str** |  | [optional] 
**bank_account_number** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auto_pay_enrollment_request import AutoPayEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoPayEnrollmentRequest from a JSON string
auto_pay_enrollment_request_instance = AutoPayEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(AutoPayEnrollmentRequest.to_json())

# convert the object into a dict
auto_pay_enrollment_request_dict = auto_pay_enrollment_request_instance.to_dict()
# create an instance of AutoPayEnrollmentRequest from a dict
auto_pay_enrollment_request_from_dict = AutoPayEnrollmentRequest.from_dict(auto_pay_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


