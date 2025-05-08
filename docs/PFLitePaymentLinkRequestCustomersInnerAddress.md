# PFLitePaymentLinkRequestCustomersInnerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **int** |  | 
**postal_code** | **str** |  | 
**time_zone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_payment_link_request_customers_inner_address import PFLitePaymentLinkRequestCustomersInnerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PFLitePaymentLinkRequestCustomersInnerAddress from a JSON string
pf_lite_payment_link_request_customers_inner_address_instance = PFLitePaymentLinkRequestCustomersInnerAddress.from_json(json)
# print the JSON string representation of the object
print(PFLitePaymentLinkRequestCustomersInnerAddress.to_json())

# convert the object into a dict
pf_lite_payment_link_request_customers_inner_address_dict = pf_lite_payment_link_request_customers_inner_address_instance.to_dict()
# create an instance of PFLitePaymentLinkRequestCustomersInnerAddress from a dict
pf_lite_payment_link_request_customers_inner_address_from_dict = PFLitePaymentLinkRequestCustomersInnerAddress.from_dict(pf_lite_payment_link_request_customers_inner_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


