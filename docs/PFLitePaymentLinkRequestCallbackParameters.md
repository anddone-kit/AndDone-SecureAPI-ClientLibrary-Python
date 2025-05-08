# PFLitePaymentLinkRequestCallbackParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_api_url** | **str** |  | [optional] 
**callback_message** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**redirection_time** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_payment_link_request_callback_parameters import PFLitePaymentLinkRequestCallbackParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PFLitePaymentLinkRequestCallbackParameters from a JSON string
pf_lite_payment_link_request_callback_parameters_instance = PFLitePaymentLinkRequestCallbackParameters.from_json(json)
# print the JSON string representation of the object
print(PFLitePaymentLinkRequestCallbackParameters.to_json())

# convert the object into a dict
pf_lite_payment_link_request_callback_parameters_dict = pf_lite_payment_link_request_callback_parameters_instance.to_dict()
# create an instance of PFLitePaymentLinkRequestCallbackParameters from a dict
pf_lite_payment_link_request_callback_parameters_from_dict = PFLitePaymentLinkRequestCallbackParameters.from_dict(pf_lite_payment_link_request_callback_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


