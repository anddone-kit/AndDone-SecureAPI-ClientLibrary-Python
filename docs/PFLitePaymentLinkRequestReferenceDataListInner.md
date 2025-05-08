# PFLitePaymentLinkRequestReferenceDataListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_type** | **str** |  | 
**reference_number** | **str** |  | [optional] 
**reference_key** | **str** |  | 

## Example

```python
from openapi_client.models.pf_lite_payment_link_request_reference_data_list_inner import PFLitePaymentLinkRequestReferenceDataListInner

# TODO update the JSON string below
json = "{}"
# create an instance of PFLitePaymentLinkRequestReferenceDataListInner from a JSON string
pf_lite_payment_link_request_reference_data_list_inner_instance = PFLitePaymentLinkRequestReferenceDataListInner.from_json(json)
# print the JSON string representation of the object
print(PFLitePaymentLinkRequestReferenceDataListInner.to_json())

# convert the object into a dict
pf_lite_payment_link_request_reference_data_list_inner_dict = pf_lite_payment_link_request_reference_data_list_inner_instance.to_dict()
# create an instance of PFLitePaymentLinkRequestReferenceDataListInner from a dict
pf_lite_payment_link_request_reference_data_list_inner_from_dict = PFLitePaymentLinkRequestReferenceDataListInner.from_dict(pf_lite_payment_link_request_reference_data_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


