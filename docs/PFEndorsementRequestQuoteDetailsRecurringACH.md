# PFEndorsementRequestQuoteDetailsRecurringACH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enroll_recurring_ach** | **bool** |  | [optional] 
**bank_routing_number** | **str** |  | [optional] 
**bank_acct_number** | **str** |  | [optional] 
**is_checking_account** | **bool** |  | [optional] 
**ach_disclosure** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pf_endorsement_request_quote_details_recurring_ach import PFEndorsementRequestQuoteDetailsRecurringACH

# TODO update the JSON string below
json = "{}"
# create an instance of PFEndorsementRequestQuoteDetailsRecurringACH from a JSON string
pf_endorsement_request_quote_details_recurring_ach_instance = PFEndorsementRequestQuoteDetailsRecurringACH.from_json(json)
# print the JSON string representation of the object
print(PFEndorsementRequestQuoteDetailsRecurringACH.to_json())

# convert the object into a dict
pf_endorsement_request_quote_details_recurring_ach_dict = pf_endorsement_request_quote_details_recurring_ach_instance.to_dict()
# create an instance of PFEndorsementRequestQuoteDetailsRecurringACH from a dict
pf_endorsement_request_quote_details_recurring_ach_from_dict = PFEndorsementRequestQuoteDetailsRecurringACH.from_dict(pf_endorsement_request_quote_details_recurring_ach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


