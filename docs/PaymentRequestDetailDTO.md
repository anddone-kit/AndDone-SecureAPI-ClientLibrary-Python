# PaymentRequestDetailDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 

## Example

```python
from openapi_client.models.payment_request_detail_dto import PaymentRequestDetailDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestDetailDTO from a JSON string
payment_request_detail_dto_instance = PaymentRequestDetailDTO.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestDetailDTO.to_json())

# convert the object into a dict
payment_request_detail_dto_dict = payment_request_detail_dto_instance.to_dict()
# create an instance of PaymentRequestDetailDTO from a dict
payment_request_detail_dto_from_dict = PaymentRequestDetailDTO.from_dict(payment_request_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


