# SecureVerifyBankAccountRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_entity_id** | **str** |  | [optional] 
**account_number** | **str** |  | 
**routing_number** | **str** |  | 
**account_holder_name** | **str** |  | [optional] 
**explicit_verification** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.secure_verify_bank_account_request_dto import SecureVerifyBankAccountRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecureVerifyBankAccountRequestDTO from a JSON string
secure_verify_bank_account_request_dto_instance = SecureVerifyBankAccountRequestDTO.from_json(json)
# print the JSON string representation of the object
print(SecureVerifyBankAccountRequestDTO.to_json())

# convert the object into a dict
secure_verify_bank_account_request_dto_dict = secure_verify_bank_account_request_dto_instance.to_dict()
# create an instance of SecureVerifyBankAccountRequestDTO from a dict
secure_verify_bank_account_request_dto_from_dict = SecureVerifyBankAccountRequestDTO.from_dict(secure_verify_bank_account_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


