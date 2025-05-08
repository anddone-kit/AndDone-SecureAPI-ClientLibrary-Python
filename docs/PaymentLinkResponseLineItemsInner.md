# PaymentLinkResponseLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_type** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**rate** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_response_line_items_inner import PaymentLinkResponseLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponseLineItemsInner from a JSON string
payment_link_response_line_items_inner_instance = PaymentLinkResponseLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponseLineItemsInner.to_json())

# convert the object into a dict
payment_link_response_line_items_inner_dict = payment_link_response_line_items_inner_instance.to_dict()
# create an instance of PaymentLinkResponseLineItemsInner from a dict
payment_link_response_line_items_inner_from_dict = PaymentLinkResponseLineItemsInner.from_dict(payment_link_response_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


