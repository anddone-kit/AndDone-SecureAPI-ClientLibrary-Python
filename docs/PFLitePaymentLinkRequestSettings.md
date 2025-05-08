# PFLitePaymentLinkRequestSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_customer_fields** | **str** |  | 
**additional_details_preference** | **str** |  | 
**display_summary** | **bool** |  | [optional] 
**accept_customer_info** | **bool** |  | [optional] 
**remove_header** | **bool** |  | [optional] 
**accept_card** | **bool** |  | [optional] 
**accept_bank_account** | **bool** |  | [optional] 
**save_customer** | **bool** |  | [optional] 
**save_customer_account** | **bool** |  | [optional] 
**intent** | [**PaymentLinkRequestSettingsIntent**](PaymentLinkRequestSettingsIntent.md) |  | 

## Example

```python
from openapi_client.models.pf_lite_payment_link_request_settings import PFLitePaymentLinkRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PFLitePaymentLinkRequestSettings from a JSON string
pf_lite_payment_link_request_settings_instance = PFLitePaymentLinkRequestSettings.from_json(json)
# print the JSON string representation of the object
print(PFLitePaymentLinkRequestSettings.to_json())

# convert the object into a dict
pf_lite_payment_link_request_settings_dict = pf_lite_payment_link_request_settings_instance.to_dict()
# create an instance of PFLitePaymentLinkRequestSettings from a dict
pf_lite_payment_link_request_settings_from_dict = PFLitePaymentLinkRequestSettings.from_dict(pf_lite_payment_link_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


