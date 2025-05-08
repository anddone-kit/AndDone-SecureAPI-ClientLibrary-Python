# VerifyBankAccountRequestBankAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.verify_bank_account_request_bank_account_entity import VerifyBankAccountRequestBankAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyBankAccountRequestBankAccountEntity from a JSON string
verify_bank_account_request_bank_account_entity_instance = VerifyBankAccountRequestBankAccountEntity.from_json(json)
# print the JSON string representation of the object
print(VerifyBankAccountRequestBankAccountEntity.to_json())

# convert the object into a dict
verify_bank_account_request_bank_account_entity_dict = verify_bank_account_request_bank_account_entity_instance.to_dict()
# create an instance of VerifyBankAccountRequestBankAccountEntity from a dict
verify_bank_account_request_bank_account_entity_from_dict = VerifyBankAccountRequestBankAccountEntity.from_dict(verify_bank_account_request_bank_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


