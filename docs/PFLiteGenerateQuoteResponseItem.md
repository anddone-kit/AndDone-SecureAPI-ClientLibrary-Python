# PFLiteGenerateQuoteResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_key** | **float** |  | [optional] 
**premium** | **float** |  | [optional] 
**down_amount** | **float** |  | [optional] 
**amount_financed** | **float** |  | [optional] 
**finance_charge** | **float** |  | [optional] 
**total_payments** | **float** |  | [optional] 
**payment_amount** | **float** |  | [optional] 
**doc_stamp** | **float** |  | [optional] 
**first_due_date** | **str** |  | [optional] 
**apr** | **float** |  | [optional] 
**installments** | **int** |  | [optional] 
**batch_id** | **str** |  | [optional] 
**payments_retained** | **float** |  | [optional] 
**payment_retained_amount** | **float** |  | [optional] 
**unsigned_pfa_url** | **str** |  | [optional] 
**retail_agent_register_login_url** | **str** |  | [optional] 
**e_sign_result** | [**PFLiteGenerateQuoteResponseItemESignResult**](PFLiteGenerateQuoteResponseItemESignResult.md) |  | [optional] 
**errors** | **str** |  | [optional] 
**pfa** | **str** |  | [optional] 
**electronic_signature_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pf_lite_generate_quote_response_item import PFLiteGenerateQuoteResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of PFLiteGenerateQuoteResponseItem from a JSON string
pf_lite_generate_quote_response_item_instance = PFLiteGenerateQuoteResponseItem.from_json(json)
# print the JSON string representation of the object
print(PFLiteGenerateQuoteResponseItem.to_json())

# convert the object into a dict
pf_lite_generate_quote_response_item_dict = pf_lite_generate_quote_response_item_instance.to_dict()
# create an instance of PFLiteGenerateQuoteResponseItem from a dict
pf_lite_generate_quote_response_item_from_dict = PFLiteGenerateQuoteResponseItem.from_dict(pf_lite_generate_quote_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


