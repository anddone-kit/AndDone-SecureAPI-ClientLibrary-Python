# MerchantTransactionEntityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_row_count** | **int** |  | [optional] 
**data** | [**List[MerchantTransactionEntityResponseDataInner]**](MerchantTransactionEntityResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_transaction_entity_response import MerchantTransactionEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantTransactionEntityResponse from a JSON string
merchant_transaction_entity_response_instance = MerchantTransactionEntityResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantTransactionEntityResponse.to_json())

# convert the object into a dict
merchant_transaction_entity_response_dict = merchant_transaction_entity_response_instance.to_dict()
# create an instance of MerchantTransactionEntityResponse from a dict
merchant_transaction_entity_response_from_dict = MerchantTransactionEntityResponse.from_dict(merchant_transaction_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


