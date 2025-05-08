# PaymentLinkResponsePfr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_response_pfr import PaymentLinkResponsePfr

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponsePfr from a JSON string
payment_link_response_pfr_instance = PaymentLinkResponsePfr.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponsePfr.to_json())

# convert the object into a dict
payment_link_response_pfr_dict = payment_link_response_pfr_instance.to_dict()
# create an instance of PaymentLinkResponsePfr from a dict
payment_link_response_pfr_from_dict = PaymentLinkResponsePfr.from_dict(payment_link_response_pfr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


