# ValidateAddressResponse

validateAddressResponse is the non error response of an address validation request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from luno_openapi.models.validate_address_response import ValidateAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAddressResponse from a JSON string
validate_address_response_instance = ValidateAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateAddressResponse.to_json())

# convert the object into a dict
validate_address_response_dict = validate_address_response_instance.to_dict()
# create an instance of ValidateAddressResponse from a dict
validate_address_response_from_dict = ValidateAddressResponse.from_dict(validate_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


