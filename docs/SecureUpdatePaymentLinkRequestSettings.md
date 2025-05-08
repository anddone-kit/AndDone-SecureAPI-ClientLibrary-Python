# SecureUpdatePaymentLinkRequestSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_customer_fields** | **str** |  | [optional] 
**additional_details_preference** | **str** |  | [optional] 
**display_summary** | **bool** |  | [optional] 
**accept_customer_info** | **bool** |  | [optional] 
**remove_header** | **bool** |  | [optional] 
**accept_card** | **bool** |  | [optional] 
**accept_bank_account** | **bool** |  | [optional] 
**save_customer** | **bool** |  | [optional] 
**save_customer_account** | **bool** |  | [optional] 
**intent** | [**SecureUpdatePaymentLinkRequestSettingsIntent**](SecureUpdatePaymentLinkRequestSettingsIntent.md) |  | [optional] 

## Example

```python
from openapi_client.models.secure_update_payment_link_request_settings import SecureUpdatePaymentLinkRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SecureUpdatePaymentLinkRequestSettings from a JSON string
secure_update_payment_link_request_settings_instance = SecureUpdatePaymentLinkRequestSettings.from_json(json)
# print the JSON string representation of the object
print(SecureUpdatePaymentLinkRequestSettings.to_json())

# convert the object into a dict
secure_update_payment_link_request_settings_dict = secure_update_payment_link_request_settings_instance.to_dict()
# create an instance of SecureUpdatePaymentLinkRequestSettings from a dict
secure_update_payment_link_request_settings_from_dict = SecureUpdatePaymentLinkRequestSettings.from_dict(secure_update_payment_link_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


