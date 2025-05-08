# PaymentBatchDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**batch_status** | **str** |  | [optional] 
**process_methods** | **str** |  | [optional] 
**processor_name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**executed_on_demand** | **bool** |  | [optional] 
**execution_time** | **str** |  | [optional] 
**completion_time** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**capture_count** | **float** |  | [optional] 
**capture_amount** | **float** |  | [optional] 
**voided_count** | **float** |  | [optional] 
**voided_amount** | **float** |  | [optional] 
**total_live_amount** | **float** |  | [optional] 
**refunded_count** | **float** |  | [optional] 
**refunded_amount** | **float** |  | [optional] 
**chargeback_count** | **float** |  | [optional] 
**chargeback_amount** | **float** |  | [optional] 
**transaction_details** | [**List[PaymentBatchDetailsResponseTransactionDetailsInner]**](PaymentBatchDetailsResponseTransactionDetailsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_batch_details_response import PaymentBatchDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBatchDetailsResponse from a JSON string
payment_batch_details_response_instance = PaymentBatchDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentBatchDetailsResponse.to_json())

# convert the object into a dict
payment_batch_details_response_dict = payment_batch_details_response_instance.to_dict()
# create an instance of PaymentBatchDetailsResponse from a dict
payment_batch_details_response_from_dict = PaymentBatchDetailsResponse.from_dict(payment_batch_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


