# PFLiteGenerateQuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**integration_id** | **str** |  | [optional] 
**item** | [**PFLiteGenerateQuoteResponseItem**](PFLiteGenerateQuoteResponseItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_generate_quote_response import PFLiteGenerateQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PFLiteGenerateQuoteResponse from a JSON string
pf_lite_generate_quote_response_instance = PFLiteGenerateQuoteResponse.from_json(json)
# print the JSON string representation of the object
print(PFLiteGenerateQuoteResponse.to_json())

# convert the object into a dict
pf_lite_generate_quote_response_dict = pf_lite_generate_quote_response_instance.to_dict()
# create an instance of PFLiteGenerateQuoteResponse from a dict
pf_lite_generate_quote_response_from_dict = PFLiteGenerateQuoteResponse.from_dict(pf_lite_generate_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


