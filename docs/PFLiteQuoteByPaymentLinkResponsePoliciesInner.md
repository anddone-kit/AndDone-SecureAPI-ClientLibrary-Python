# PFLiteQuoteByPaymentLinkResponsePoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**policy_number** | **str** |  | [optional] 
**premium** | **float** |  | [optional] 
**additional_fees** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**coverage_type** | **str** |  | [optional] 
**effective_date** | **str** |  | [optional] 
**cancel_days** | **str** |  | [optional] 
**minimum_earned_percent** | **float** |  | [optional] 
**carrier** | [**PFLiteQuoteByPaymentLinkResponsePoliciesInnerCarrier**](PFLiteQuoteByPaymentLinkResponsePoliciesInnerCarrier.md) |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**term** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_quote_by_payment_link_response_policies_inner import PFLiteQuoteByPaymentLinkResponsePoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PFLiteQuoteByPaymentLinkResponsePoliciesInner from a JSON string
pf_lite_quote_by_payment_link_response_policies_inner_instance = PFLiteQuoteByPaymentLinkResponsePoliciesInner.from_json(json)
# print the JSON string representation of the object
print(PFLiteQuoteByPaymentLinkResponsePoliciesInner.to_json())

# convert the object into a dict
pf_lite_quote_by_payment_link_response_policies_inner_dict = pf_lite_quote_by_payment_link_response_policies_inner_instance.to_dict()
# create an instance of PFLiteQuoteByPaymentLinkResponsePoliciesInner from a dict
pf_lite_quote_by_payment_link_response_policies_inner_from_dict = PFLiteQuoteByPaymentLinkResponsePoliciesInner.from_dict(pf_lite_quote_by_payment_link_response_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


