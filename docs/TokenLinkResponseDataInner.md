# TokenLinkResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | [optional] 
**token_link_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**expire_on** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**token_link_status** | **str** |  | [optional] 
**response_type** | **str** |  | [optional] 
**call_back_parameters** | [**PaymentLinkResponseCallbackParameters**](PaymentLinkResponseCallbackParameters.md) |  | [optional] 
**intent** | [**SecureTokenLinkResponseIntent**](SecureTokenLinkResponseIntent.md) |  | [optional] 
**customers** | [**List[SecureTokenLinkResponseCustomersInner]**](SecureTokenLinkResponseCustomersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.token_link_response_data_inner import TokenLinkResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkResponseDataInner from a JSON string
token_link_response_data_inner_instance = TokenLinkResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(TokenLinkResponseDataInner.to_json())

# convert the object into a dict
token_link_response_data_inner_dict = token_link_response_data_inner_instance.to_dict()
# create an instance of TokenLinkResponseDataInner from a dict
token_link_response_data_inner_from_dict = TokenLinkResponseDataInner.from_dict(token_link_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


