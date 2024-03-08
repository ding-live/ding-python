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

s = ding.Ding(
    api_key="YOUR_API_KEY",
)


res = s.lookup.lookup(phone_number='<value>', customer_uuid='6e93aa15-9177-4d09-8395-b69ce50db1c8')

if res.lookup_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `phone_number`     | *str*              | :heavy_check_mark: | N/A                |
| `customer_uuid`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.LookupResponse](../../models/operations/lookupresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4x-5xx               | */*                  |
