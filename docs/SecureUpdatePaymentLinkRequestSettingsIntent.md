# SecureUpdatePaymentLinkRequestSettingsIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_types** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.secure_update_payment_link_request_settings_intent import SecureUpdatePaymentLinkRequestSettingsIntent

# TODO update the JSON string below
json = "{}"
# create an instance of SecureUpdatePaymentLinkRequestSettingsIntent from a JSON string
secure_update_payment_link_request_settings_intent_instance = SecureUpdatePaymentLinkRequestSettingsIntent.from_json(json)
# print the JSON string representation of the object
print(SecureUpdatePaymentLinkRequestSettingsIntent.to_json())

# convert the object into a dict
secure_update_payment_link_request_settings_intent_dict = secure_update_payment_link_request_settings_intent_instance.to_dict()
# create an instance of SecureUpdatePaymentLinkRequestSettingsIntent from a dict
secure_update_payment_link_request_settings_intent_from_dict = SecureUpdatePaymentLinkRequestSettingsIntent.from_dict(secure_update_payment_link_request_settings_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


