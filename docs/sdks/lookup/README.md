# Lookup
(*.lookup*)

## Overview

Retrieve up-to-date metadata about a specific phone number

### Available Operations

* [post_lookup](#post_lookup) - Lookup a phone number

## post_lookup

Lookup a phone number

### Example Usage

```python
import ding
from ding.models import operations, shared

s = ding.Ding(
    api_key="",
)


res = s.lookup.post_lookup(customer_uuid='0959c29c-3ae6-483a-89ec-d21e646d9da9', lookup_request=shared.LookupRequest(
    phone_number='+1234567890',
))

if res.lookup_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `customer_uuid`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `lookup_request`                                                       | [Optional[shared.LookupRequest]](../../models/shared/lookuprequest.md) | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.PostLookupResponse](../../models/operations/postlookupresponse.md)**

