# TokenLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_row_count** | **int** |  | [optional] 
**data** | [**List[TokenLinkResponseDataInner]**](TokenLinkResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.token_link_response import TokenLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkResponse from a JSON string
token_link_response_instance = TokenLinkResponse.from_json(json)
# print the JSON string representation of the object
print(TokenLinkResponse.to_json())

# convert the object into a dict
token_link_response_dict = token_link_response_instance.to_dict()
# create an instance of TokenLinkResponse from a dict
token_link_response_from_dict = TokenLinkResponse.from_dict(token_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


