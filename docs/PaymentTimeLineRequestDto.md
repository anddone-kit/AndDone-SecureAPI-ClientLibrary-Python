# PaymentTimeLineRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 

## Example

```python
from openapi_client.models.payment_time_line_request_dto import PaymentTimeLineRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTimeLineRequestDto from a JSON string
payment_time_line_request_dto_instance = PaymentTimeLineRequestDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTimeLineRequestDto.to_json())

# convert the object into a dict
payment_time_line_request_dto_dict = payment_time_line_request_dto_instance.to_dict()
# create an instance of PaymentTimeLineRequestDto from a dict
payment_time_line_request_dto_from_dict = PaymentTimeLineRequestDto.from_dict(payment_time_line_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


