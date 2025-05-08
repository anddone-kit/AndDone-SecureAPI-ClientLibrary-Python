# QuoteRequestInsured


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_customer_number** | **str** |  | [optional] 
**email** | **str** |  | 
**care_of** | **str** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**address** | [**QuoteRequestInsuredAddress**](QuoteRequestInsuredAddress.md) |  | 
**has_data_change_agent_customer_number** | **bool** |  | [optional] 
**has_data_change_name** | **bool** |  | [optional] 
**has_data_change_address1** | **bool** |  | [optional] 
**has_data_change_address2** | **bool** |  | [optional] 
**has_data_change_city** | **bool** |  | [optional] 
**has_data_change_state** | **bool** |  | [optional] 
**has_data_change_zip** | **bool** |  | [optional] 
**has_data_change_phone** | **bool** |  | [optional] 
**has_data_change_email** | **bool** |  | [optional] 
**has_data_change_care_of** | **bool** |  | [optional] 
**has_data_change_insured** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.quote_request_insured import QuoteRequestInsured

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRequestInsured from a JSON string
quote_request_insured_instance = QuoteRequestInsured.from_json(json)
# print the JSON string representation of the object
print(QuoteRequestInsured.to_json())

# convert the object into a dict
quote_request_insured_dict = quote_request_insured_instance.to_dict()
# create an instance of QuoteRequestInsured from a dict
quote_request_insured_from_dict = QuoteRequestInsured.from_dict(quote_request_insured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


