# VerifyBankAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**routing_number** | **str** |  | 
**account_holder_name** | **str** |  | 
**statement_display_name** | **str** |  | [optional] 
**bank_account_entity** | [**VerifyBankAccountRequestBankAccountEntity**](VerifyBankAccountRequestBankAccountEntity.md) |  | [optional] 

## Example

```python
from openapi_client.models.verify_bank_account_request import VerifyBankAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyBankAccountRequest from a JSON string
verify_bank_account_request_instance = VerifyBankAccountRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyBankAccountRequest.to_json())

# convert the object into a dict
verify_bank_account_request_dict = verify_bank_account_request_instance.to_dict()
# create an instance of VerifyBankAccountRequest from a dict
verify_bank_account_request_from_dict = VerifyBankAccountRequest.from_dict(verify_bank_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


