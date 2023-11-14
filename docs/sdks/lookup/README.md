# Lookup
(*lookup*)

## Overview

Retrieve up-to-date metadata about a specific phone number

### Available Operations

* [lookup](#lookup) - Perform a phone number lookup

## lookup

Perform a phone number lookup

### Example Usage

```python
import ding
from ding.models import operations

s = ding.Ding(
    api_key="YOUR_API_KEY",
)


res = s.lookup.lookup(customer_uuid='6e93aa15-9177-4d09-8395-b69ce50db1c8', phone_number='string')

if res.lookup_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `customer_uuid`    | *str*              | :heavy_check_mark: | N/A                |
| `phone_number`     | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.LookupResponse](../../models/operations/lookupresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |
