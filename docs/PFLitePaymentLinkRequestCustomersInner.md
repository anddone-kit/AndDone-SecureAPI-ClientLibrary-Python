# PFLitePaymentLinkRequestCustomersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**phone_country_code** | **str** |  | [optional] 
**address** | [**PFLitePaymentLinkRequestCustomersInnerAddress**](PFLitePaymentLinkRequestCustomersInnerAddress.md) |  | [optional] 
**notify_via_sms** | **bool** |  | [optional] 
**notify_via_email** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_payment_link_request_customers_inner import PFLitePaymentLinkRequestCustomersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PFLitePaymentLinkRequestCustomersInner from a JSON string
pf_lite_payment_link_request_customers_inner_instance = PFLitePaymentLinkRequestCustomersInner.from_json(json)
# print the JSON string representation of the object
print(PFLitePaymentLinkRequestCustomersInner.to_json())

# convert the object into a dict
pf_lite_payment_link_request_customers_inner_dict = pf_lite_payment_link_request_customers_inner_instance.to_dict()
# create an instance of PFLitePaymentLinkRequestCustomersInner from a dict
pf_lite_payment_link_request_customers_inner_from_dict = PFLitePaymentLinkRequestCustomersInner.from_dict(pf_lite_payment_link_request_customers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


