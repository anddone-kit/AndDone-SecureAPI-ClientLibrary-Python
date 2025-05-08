# CancelPaymentRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 

## Example

```python
from openapi_client.models.cancel_payment_request_dto import CancelPaymentRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPaymentRequestDTO from a JSON string
cancel_payment_request_dto_instance = CancelPaymentRequestDTO.from_json(json)
# print the JSON string representation of the object
print(CancelPaymentRequestDTO.to_json())

# convert the object into a dict
cancel_payment_request_dto_dict = cancel_payment_request_dto_instance.to_dict()
# create an instance of CancelPaymentRequestDTO from a dict
cancel_payment_request_dto_from_dict = CancelPaymentRequestDTO.from_dict(cancel_payment_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


