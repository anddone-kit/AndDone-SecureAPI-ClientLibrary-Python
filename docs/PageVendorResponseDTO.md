# PageVendorResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_row_count** | **int** |  | [optional] 
**data** | [**List[PageVendorResponseDTODataInner]**](PageVendorResponseDTODataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.page_vendor_response_dto import PageVendorResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PageVendorResponseDTO from a JSON string
page_vendor_response_dto_instance = PageVendorResponseDTO.from_json(json)
# print the JSON string representation of the object
print(PageVendorResponseDTO.to_json())

# convert the object into a dict
page_vendor_response_dto_dict = page_vendor_response_dto_instance.to_dict()
# create an instance of PageVendorResponseDTO from a dict
page_vendor_response_dto_from_dict = PageVendorResponseDTO.from_dict(page_vendor_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


