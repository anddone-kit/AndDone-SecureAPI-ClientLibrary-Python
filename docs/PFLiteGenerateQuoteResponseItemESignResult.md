# PFLiteGenerateQuoteResponseItemESignResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**batch_id** | **str** |  | [optional] 
**agent_url** | **str** |  | [optional] 
**insured_url** | **str** |  | [optional] 
**e_sign_option** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_generate_quote_response_item_e_sign_result import PFLiteGenerateQuoteResponseItemESignResult

# TODO update the JSON string below
json = "{}"
# create an instance of PFLiteGenerateQuoteResponseItemESignResult from a JSON string
pf_lite_generate_quote_response_item_e_sign_result_instance = PFLiteGenerateQuoteResponseItemESignResult.from_json(json)
# print the JSON string representation of the object
print(PFLiteGenerateQuoteResponseItemESignResult.to_json())

# convert the object into a dict
pf_lite_generate_quote_response_item_e_sign_result_dict = pf_lite_generate_quote_response_item_e_sign_result_instance.to_dict()
# create an instance of PFLiteGenerateQuoteResponseItemESignResult from a dict
pf_lite_generate_quote_response_item_e_sign_result_from_dict = PFLiteGenerateQuoteResponseItemESignResult.from_dict(pf_lite_generate_quote_response_item_e_sign_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


