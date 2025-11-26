# PagePaymentListResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_row_count** | **int** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**data** | [**List[PagePaymentListResponseDTODataInner]**](PagePaymentListResponseDTODataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.page_payment_list_response_dto import PagePaymentListResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PagePaymentListResponseDTO from a JSON string
page_payment_list_response_dto_instance = PagePaymentListResponseDTO.from_json(json)
# print the JSON string representation of the object
print(PagePaymentListResponseDTO.to_json())

# convert the object into a dict
page_payment_list_response_dto_dict = page_payment_list_response_dto_instance.to_dict()
# create an instance of PagePaymentListResponseDTO from a dict
page_payment_list_response_dto_from_dict = PagePaymentListResponseDTO.from_dict(page_payment_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


