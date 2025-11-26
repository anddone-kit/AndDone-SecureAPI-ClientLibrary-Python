# PFLiteSecureQuoteRequestAgentAddress

This denotes the address of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_secure_quote_request_agent_address import PFLiteSecureQuoteRequestAgentAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PFLiteSecureQuoteRequestAgentAddress from a JSON string
pf_lite_secure_quote_request_agent_address_instance = PFLiteSecureQuoteRequestAgentAddress.from_json(json)
# print the JSON string representation of the object
print(PFLiteSecureQuoteRequestAgentAddress.to_json())

# convert the object into a dict
pf_lite_secure_quote_request_agent_address_dict = pf_lite_secure_quote_request_agent_address_instance.to_dict()
# create an instance of PFLiteSecureQuoteRequestAgentAddress from a dict
pf_lite_secure_quote_request_agent_address_from_dict = PFLiteSecureQuoteRequestAgentAddress.from_dict(pf_lite_secure_quote_request_agent_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


