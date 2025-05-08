# VerifyBankAccountResponseHttpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success_status_code** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**status_code** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.verify_bank_account_response_http_response import VerifyBankAccountResponseHttpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyBankAccountResponseHttpResponse from a JSON string
verify_bank_account_response_http_response_instance = VerifyBankAccountResponseHttpResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyBankAccountResponseHttpResponse.to_json())

# convert the object into a dict
verify_bank_account_response_http_response_dict = verify_bank_account_response_http_response_instance.to_dict()
# create an instance of VerifyBankAccountResponseHttpResponse from a dict
verify_bank_account_response_http_response_from_dict = VerifyBankAccountResponseHttpResponse.from_dict(verify_bank_account_response_http_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


