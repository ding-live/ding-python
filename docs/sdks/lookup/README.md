# Lookup
(*lookup*)

## Overview

Retrieve up-to-date metadata about a specific phone number

### Available Operations

* [lookup](#lookup) - Lookup a phone number

## lookup

Lookup a phone number

### Example Usage

```python
import ding
from ding.models import components, operations

s = ding.Ding(
    api_key="YOUR_API_KEY",
)


res = s.lookup.lookup(customer_uuid='6e93aa15-9177-4d09-8395-b69ce50db1c8', lookup_request=components.LookupRequest(
    phone_number='+1234567890',
))

if res.lookup_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `customer_uuid`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `lookup_request`                                                               | [Optional[components.LookupRequest]](../../models/components/lookuprequest.md) | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.LookupResponse](../../models/operations/lookupresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |
