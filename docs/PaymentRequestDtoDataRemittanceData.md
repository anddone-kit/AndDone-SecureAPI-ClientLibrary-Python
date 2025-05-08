# PaymentRequestDtoDataRemittanceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headings** | [**List[HeadingDto]**](HeadingDto.md) |  | [optional] 
**rows** | **List[List[RowDto]]** |  | [optional] 

## Example

```python
from openapi_client.models.payment_request_dto_data_remittance_data import PaymentRequestDtoDataRemittanceData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestDtoDataRemittanceData from a JSON string
payment_request_dto_data_remittance_data_instance = PaymentRequestDtoDataRemittanceData.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestDtoDataRemittanceData.to_json())

# convert the object into a dict
payment_request_dto_data_remittance_data_dict = payment_request_dto_data_remittance_data_instance.to_dict()
# create an instance of PaymentRequestDtoDataRemittanceData from a dict
payment_request_dto_data_remittance_data_from_dict = PaymentRequestDtoDataRemittanceData.from_dict(payment_request_dto_data_remittance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


