# QuoteRequestAgentAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quote_request_agent_address import QuoteRequestAgentAddress

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRequestAgentAddress from a JSON string
quote_request_agent_address_instance = QuoteRequestAgentAddress.from_json(json)
# print the JSON string representation of the object
print(QuoteRequestAgentAddress.to_json())

# convert the object into a dict
quote_request_agent_address_dict = quote_request_agent_address_instance.to_dict()
# create an instance of QuoteRequestAgentAddress from a dict
quote_request_agent_address_from_dict = QuoteRequestAgentAddress.from_dict(quote_request_agent_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


