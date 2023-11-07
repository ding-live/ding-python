# Otp
(*.otp*)

## Overview

Send OTP codes to your users using their phone numbers.

### Available Operations

* [check](#check) - Check an authentication code
* [create_autentication](#create_autentication) - Create an authentication
* [retry](#retry) - Retry an authentication

## check

Check an authentication code

### Example Usage

```python
import test
from test.models import components

s = test.Test(
    api_key="YOUR_API_KEY",
)

req = components.CreateCheckRequest(
    authentication_uuid='e0e7b0e9-739d-424b-922f-1c2cb48ab077',
    check_code='123456',
    customer_uuid='8f1196d5-806e-4b71-9b24-5f96ec052808',
)

res = s.otp.check(req)

if res.create_check_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.CreateCheckRequest](../../models/shared/createcheckrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CheckResponse](../../models/operations/checkresponse.md)**


## create_autentication

Create an authentication

### Example Usage

```python
import test
from test.models import components

s = test.Test(
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    app_realm='1234567890',
    app_version='1.0.0',
    callback_url='https://example.com/callback',
    customer_uuid='eae192ab-9e1e-4b21-b5b1-bfcb79a32fcc',
    device_id='1234567890',
    device_model='iPhone 15 Pro',
    os_version='13.2.1',
    phone_number='+1234567890',
)

res = s.otp.create_autentication(req)

if res.create_authentication_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.CreateAuthenticationRequest](../../models/shared/createauthenticationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateAutenticationResponse](../../models/operations/createautenticationresponse.md)**


## retry

Retry an authentication

### Example Usage

```python
import test
from test.models import components

s = test.Test(
    api_key="YOUR_API_KEY",
)

req = components.RetryAuthenticationRequest(
    authentication_uuid='a74ee547-564d-487a-91df-37fb25413a91',
    customer_uuid='3c8b3a46-881e-4cdd-93a6-f7f238bf020a',
)

res = s.otp.retry(req)

if res.retry_authentication_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.RetryAuthenticationRequest](../../models/shared/retryauthenticationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RetryResponse](../../models/operations/retryresponse.md)**

