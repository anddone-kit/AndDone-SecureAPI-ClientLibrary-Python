# PaymentListResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**merchant_dba_name** | **str** |  | [optional] 
**payment_method_type** | **str** |  | [optional] 
**payment_based_id** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**payment_method_status** | **str** |  | [optional] 
**requested_date** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_list_response_dto import PaymentListResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentListResponseDTO from a JSON string
payment_list_response_dto_instance = PaymentListResponseDTO.from_json(json)
# print the JSON string representation of the object
print(PaymentListResponseDTO.to_json())

# convert the object into a dict
payment_list_response_dto_dict = payment_list_response_dto_instance.to_dict()
# create an instance of PaymentListResponseDTO from a dict
payment_list_response_dto_from_dict = PaymentListResponseDTO.from_dict(payment_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


