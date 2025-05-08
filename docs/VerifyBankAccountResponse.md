# VerifyBankAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**verification_entity_id** | **str** |  | [optional] 
**verifying_entity** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**status_reason** | **str** |  | [optional] 
**estimated_verification_date** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**bank_account_entity_id** | **float** |  | [optional] 
**bank_account_entity_type** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**http_response** | [**VerifyBankAccountResponseHttpResponse**](VerifyBankAccountResponseHttpResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.verify_bank_account_response import VerifyBankAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyBankAccountResponse from a JSON string
verify_bank_account_response_instance = VerifyBankAccountResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyBankAccountResponse.to_json())

# convert the object into a dict
verify_bank_account_response_dict = verify_bank_account_response_instance.to_dict()
# create an instance of VerifyBankAccountResponse from a dict
verify_bank_account_response_from_dict = VerifyBankAccountResponse.from_dict(verify_bank_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


