# PFEndorsementRequestQuoteInsured


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_customer_number** | **str** | This denotes the Agent Customer Number. | [optional] 
**email** | **str** | This denotes the email. | [optional] 
**care_of** | **str** | This denotes the care of. | [optional] 
**unique_id** | **str** | This denotes a unique identifier for the insured. | [optional] 
**mobile_phone_number** | **str** | This denotes the mobile phone number. | [optional] 
**is_cancellation_warning_enabled** | **bool** | Indicates if cancellation warnings are enabled. | [optional] 
**fax_number** | **str** | This denotes the fax number. | [optional] 
**email_address** | **str** | This denotes an alternate email address. | [optional] 
**pf_type** | **str** | This denotes the PFType (enum or string depending on your definition). | [optional] 
**address** | [**PFEndorsementRequestQuoteInsuredAddress**](PFEndorsementRequestQuoteInsuredAddress.md) |  | [optional] 
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
from openapi_client.models.pf_endorsement_request_quote_insured import PFEndorsementRequestQuoteInsured

# TODO update the JSON string below
json = "{}"
# create an instance of PFEndorsementRequestQuoteInsured from a JSON string
pf_endorsement_request_quote_insured_instance = PFEndorsementRequestQuoteInsured.from_json(json)
# print the JSON string representation of the object
print(PFEndorsementRequestQuoteInsured.to_json())

# convert the object into a dict
pf_endorsement_request_quote_insured_dict = pf_endorsement_request_quote_insured_instance.to_dict()
# create an instance of PFEndorsementRequestQuoteInsured from a dict
pf_endorsement_request_quote_insured_from_dict = PFEndorsementRequestQuoteInsured.from_dict(pf_endorsement_request_quote_insured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


