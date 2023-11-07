# Otp
(*.otp*)

## Overview

Send OTP codes to your users using their phone numbers.

### Available Operations

* [post_authentication](#post_authentication) - Create an authentication
* [post_check](#post_check) - Check an authentication code
* [post_retry](#post_retry) - Retry an authentication

## post_authentication

Create an authentication

### Example Usage

```python
import ding
from ding.models import shared

s = ding.Ding(
    api_key="",
)

req = shared.CreateAuthenticationRequest(
    app_realm='1234567890',
    app_version='1.0.0',
    callback_url='https://example.com/callback',
    customer_uuid='28591d9e-a825-47f6-ab11-1a61726305bf',
    device_id='1234567890',
    device_model='iPhone 15 Pro',
    os_version='13.2.1',
    phone_number='+1234567890',
)

res = s.otp.post_authentication(req)

if res.create_authentication_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateAuthenticationRequest](../../models/shared/createauthenticationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostAuthenticationResponse](../../models/operations/postauthenticationresponse.md)**


## post_check

Check an authentication code

### Example Usage

```python
import ding
from ding.models import shared

s = ding.Ding(
    api_key="",
)

req = shared.CreateCheckRequest(
    authentication_uuid='b96e4807-1510-4bd2-8106-8ca1a09d679e',
    check_code='123456',
    customer_uuid='b193166e-1ee3-41d3-9acb-9c9ac7f10712',
)

res = s.otp.post_check(req)

if res.create_check_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.CreateCheckRequest](../../models/shared/createcheckrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostCheckResponse](../../models/operations/postcheckresponse.md)**


## post_retry

Retry an authentication

### Example Usage

```python
import ding
from ding.models import shared

s = ding.Ding(
    api_key="",
)

req = shared.RetryAuthenticationRequest(
    authentication_uuid='32ca23f2-1d21-434e-a8c9-89320993ec98',
    customer_uuid='f5d6d1dc-4ce6-4232-8707-1b4af2d537d4',
)

res = s.otp.post_retry(req)

if res.retry_authentication_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.RetryAuthenticationRequest](../../models/shared/retryauthenticationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PostRetryResponse](../../models/operations/postretryresponse.md)**

