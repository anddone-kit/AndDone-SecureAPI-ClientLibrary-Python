# TokenLinkSecureRequestCallbackParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_success_url** | **str** |  | [optional] 
**callback_failure_url** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**callback_api_url** | **str** |  | [optional] 
**callback_message** | **str** |  | [optional] 
**redirection_time** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.token_link_secure_request_callback_parameters import TokenLinkSecureRequestCallbackParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkSecureRequestCallbackParameters from a JSON string
token_link_secure_request_callback_parameters_instance = TokenLinkSecureRequestCallbackParameters.from_json(json)
# print the JSON string representation of the object
print(TokenLinkSecureRequestCallbackParameters.to_json())

# convert the object into a dict
token_link_secure_request_callback_parameters_dict = token_link_secure_request_callback_parameters_instance.to_dict()
# create an instance of TokenLinkSecureRequestCallbackParameters from a dict
token_link_secure_request_callback_parameters_from_dict = TokenLinkSecureRequestCallbackParameters.from_dict(token_link_secure_request_callback_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


