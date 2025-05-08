# PagePaymentListResponseDTODataInner


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
from openapi_client.models.page_payment_list_response_dto_data_inner import PagePaymentListResponseDTODataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PagePaymentListResponseDTODataInner from a JSON string
page_payment_list_response_dto_data_inner_instance = PagePaymentListResponseDTODataInner.from_json(json)
# print the JSON string representation of the object
print(PagePaymentListResponseDTODataInner.to_json())

# convert the object into a dict
page_payment_list_response_dto_data_inner_dict = page_payment_list_response_dto_data_inner_instance.to_dict()
# create an instance of PagePaymentListResponseDTODataInner from a dict
page_payment_list_response_dto_data_inner_from_dict = PagePaymentListResponseDTODataInner.from_dict(page_payment_list_response_dto_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


