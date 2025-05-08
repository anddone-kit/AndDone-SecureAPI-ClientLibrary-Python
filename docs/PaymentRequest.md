# PaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**type** | **str** |  | 
**transaction_code** | **str** |  | 
**billing_contact** | [**TransactionPaymentResponseBillingContact**](TransactionPaymentResponseBillingContact.md) |  | [optional] 
**phone_country_code** | **str** |  | [optional] 
**channel_type** | **str** |  | 
**process_method** | **str** |  | [optional] 
**tender_info** | [**PaymentRequestTenderInfo**](PaymentRequestTenderInfo.md) |  | 
**invoice_no** | **str** |  | [optional] 
**reference_no** | **str** |  | [optional] 
**payment_reference** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**save_customer** | **bool** |  | [optional] 
**captcha_token** | **str** |  | [optional] 
**action_name** | **str** |  | [optional] 
**additional_fields** | **Dict[str, str]** |  | [optional] 
**issuer** | **str** |  | [optional] 
**splits** | [**List[PaymentIntentRequestSplitsInner]**](PaymentIntentRequestSplitsInner.md) |  | [optional] 
**operation_type** | **str** |  | [optional] 
**suppress_technology_fee** | **bool** |  | [optional] 
**override_technology_fee** | **float** |  | [optional] 
**is_premium_financier** | **bool** |  | [optional] 
**pfr** | [**PaymentIntentRequestPfr**](PaymentIntentRequestPfr.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_request import PaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequest from a JSON string
payment_request_instance = PaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentRequest.to_json())

# convert the object into a dict
payment_request_dict = payment_request_instance.to_dict()
# create an instance of PaymentRequest from a dict
payment_request_from_dict = PaymentRequest.from_dict(payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


