# QuoteRequestPoliciesInnerGaAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**zip** | **str** |  | 
**phone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quote_request_policies_inner_ga_address import QuoteRequestPoliciesInnerGaAddress

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRequestPoliciesInnerGaAddress from a JSON string
quote_request_policies_inner_ga_address_instance = QuoteRequestPoliciesInnerGaAddress.from_json(json)
# print the JSON string representation of the object
print(QuoteRequestPoliciesInnerGaAddress.to_json())

# convert the object into a dict
quote_request_policies_inner_ga_address_dict = quote_request_policies_inner_ga_address_instance.to_dict()
# create an instance of QuoteRequestPoliciesInnerGaAddress from a dict
quote_request_policies_inner_ga_address_from_dict = QuoteRequestPoliciesInnerGaAddress.from_dict(quote_request_policies_inner_ga_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


