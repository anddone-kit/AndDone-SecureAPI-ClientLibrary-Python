# PaymentRequestDtoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_number** | **int** |  | [optional] 
**memo** | **str** |  | [optional] 
**check_date** | **str** |  | [optional] 
**remittance_data** | [**PaymentRequestDtoDataRemittanceData**](PaymentRequestDtoDataRemittanceData.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_request_dto_data import PaymentRequestDtoData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestDtoData from a JSON string
payment_request_dto_data_instance = PaymentRequestDtoData.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestDtoData.to_json())

# convert the object into a dict
payment_request_dto_data_dict = payment_request_dto_data_instance.to_dict()
# create an instance of PaymentRequestDtoData from a dict
payment_request_dto_data_from_dict = PaymentRequestDtoData.from_dict(payment_request_dto_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


