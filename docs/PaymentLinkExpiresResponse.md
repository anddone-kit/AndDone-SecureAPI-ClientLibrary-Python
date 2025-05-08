# PaymentLinkExpiresResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_expires_response import PaymentLinkExpiresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkExpiresResponse from a JSON string
payment_link_expires_response_instance = PaymentLinkExpiresResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkExpiresResponse.to_json())

# convert the object into a dict
payment_link_expires_response_dict = payment_link_expires_response_instance.to_dict()
# create an instance of PaymentLinkExpiresResponse from a dict
payment_link_expires_response_from_dict = PaymentLinkExpiresResponse.from_dict(payment_link_expires_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


