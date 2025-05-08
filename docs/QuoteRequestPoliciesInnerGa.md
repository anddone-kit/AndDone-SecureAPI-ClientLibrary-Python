# QuoteRequestPoliciesInnerGa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | 
**name** | **str** |  | [optional] 
**care_of** | **str** |  | [optional] 
**is_validation_required** | **bool** |  | [optional] 
**address** | [**QuoteRequestPoliciesInnerGaAddress**](QuoteRequestPoliciesInnerGaAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.quote_request_policies_inner_ga import QuoteRequestPoliciesInnerGa

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRequestPoliciesInnerGa from a JSON string
quote_request_policies_inner_ga_instance = QuoteRequestPoliciesInnerGa.from_json(json)
# print the JSON string representation of the object
print(QuoteRequestPoliciesInnerGa.to_json())

# convert the object into a dict
quote_request_policies_inner_ga_dict = quote_request_policies_inner_ga_instance.to_dict()
# create an instance of QuoteRequestPoliciesInnerGa from a dict
quote_request_policies_inner_ga_from_dict = QuoteRequestPoliciesInnerGa.from_dict(quote_request_policies_inner_ga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


