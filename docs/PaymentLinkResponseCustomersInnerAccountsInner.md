# PaymentLinkResponseCustomersInnerAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**card_number** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**account_token** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**is_checking_account** | **bool** |  | [optional] 
**is_expired** | **bool** |  | [optional] 
**created_on** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_response_customers_inner_accounts_inner import PaymentLinkResponseCustomersInnerAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponseCustomersInnerAccountsInner from a JSON string
payment_link_response_customers_inner_accounts_inner_instance = PaymentLinkResponseCustomersInnerAccountsInner.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponseCustomersInnerAccountsInner.to_json())

# convert the object into a dict
payment_link_response_customers_inner_accounts_inner_dict = payment_link_response_customers_inner_accounts_inner_instance.to_dict()
# create an instance of PaymentLinkResponseCustomersInnerAccountsInner from a dict
payment_link_response_customers_inner_accounts_inner_from_dict = PaymentLinkResponseCustomersInnerAccountsInner.from_dict(payment_link_response_customers_inner_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


