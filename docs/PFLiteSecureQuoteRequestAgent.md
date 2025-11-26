# PFLiteSecureQuoteRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | This denotes the Unique ID. | [optional] 
**email** | **str** | This denotes the email of the agent. | [optional] 
**care_of** | **str** | This denotes the CareOf of the agent. | [optional] 
**address** | [**PFLiteSecureQuoteRequestAgentAddress**](PFLiteSecureQuoteRequestAgentAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_secure_quote_request_agent import PFLiteSecureQuoteRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PFLiteSecureQuoteRequestAgent from a JSON string
pf_lite_secure_quote_request_agent_instance = PFLiteSecureQuoteRequestAgent.from_json(json)
# print the JSON string representation of the object
print(PFLiteSecureQuoteRequestAgent.to_json())

# convert the object into a dict
pf_lite_secure_quote_request_agent_dict = pf_lite_secure_quote_request_agent_instance.to_dict()
# create an instance of PFLiteSecureQuoteRequestAgent from a dict
pf_lite_secure_quote_request_agent_from_dict = PFLiteSecureQuoteRequestAgent.from_dict(pf_lite_secure_quote_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


