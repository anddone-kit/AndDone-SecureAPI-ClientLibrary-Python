# VendorTimelineResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_status** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**event_date** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.vendor_timeline_response_list_inner import VendorTimelineResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorTimelineResponseListInner from a JSON string
vendor_timeline_response_list_inner_instance = VendorTimelineResponseListInner.from_json(json)
# print the JSON string representation of the object
print(VendorTimelineResponseListInner.to_json())

# convert the object into a dict
vendor_timeline_response_list_inner_dict = vendor_timeline_response_list_inner_instance.to_dict()
# create an instance of VendorTimelineResponseListInner from a dict
vendor_timeline_response_list_inner_from_dict = VendorTimelineResponseListInner.from_dict(vendor_timeline_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


