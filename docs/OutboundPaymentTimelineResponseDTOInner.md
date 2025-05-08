# OutboundPaymentTimelineResponseDTOInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_status** | **str** |  | [optional] 
**payment_method_status** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.outbound_payment_timeline_response_dto_inner import OutboundPaymentTimelineResponseDTOInner

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundPaymentTimelineResponseDTOInner from a JSON string
outbound_payment_timeline_response_dto_inner_instance = OutboundPaymentTimelineResponseDTOInner.from_json(json)
# print the JSON string representation of the object
print(OutboundPaymentTimelineResponseDTOInner.to_json())

# convert the object into a dict
outbound_payment_timeline_response_dto_inner_dict = outbound_payment_timeline_response_dto_inner_instance.to_dict()
# create an instance of OutboundPaymentTimelineResponseDTOInner from a dict
outbound_payment_timeline_response_dto_inner_from_dict = OutboundPaymentTimelineResponseDTOInner.from_dict(outbound_payment_timeline_response_dto_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


