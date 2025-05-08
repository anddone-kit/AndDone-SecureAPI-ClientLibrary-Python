# PFRetrievePFAResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pfa** | **str** | The PFA document. | [optional] 
**mimetype** | **str** | The MIME type of the PFA document. | [optional] 
**extension** | **str** | The file extension of the PFA document. | [optional] 
**filename** | **str** | The filename of the PFA document. | [optional] 
**message** | **str** | A message related to the PFA retrieval. | [optional] 
**is_success** | **bool** | Indicates if the retrieval was successful. | [optional] 
**integration_id** | **str** | The integration ID associated with the PFA retrieval. | [optional] 

## Example

```python
from openapi_client.models.pf_retrieve_pfa_response import PFRetrievePFAResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PFRetrievePFAResponse from a JSON string
pf_retrieve_pfa_response_instance = PFRetrievePFAResponse.from_json(json)
# print the JSON string representation of the object
print(PFRetrievePFAResponse.to_json())

# convert the object into a dict
pf_retrieve_pfa_response_dict = pf_retrieve_pfa_response_instance.to_dict()
# create an instance of PFRetrievePFAResponse from a dict
pf_retrieve_pfa_response_from_dict = PFRetrievePFAResponse.from_dict(pf_retrieve_pfa_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


