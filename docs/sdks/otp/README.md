# Otp
(*otp*)

## Overview

Send OTP codes to your users using their phone numbers.

### Available Operations

* [check](#check) - Check an authentication code
* [retry](#retry) - Retry an authentication
* [send](#send) - Create an authentication

## check

Check an authentication code

### Example Usage

```python
import ding
from ding.models import components

s = ding.Ding(
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

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.CreateCheckRequest](../../models/components/createcheckrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CheckResponse](../../models/operations/checkresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |

## retry

Retry an authentication

### Example Usage

```python
import ding
from ding.models import components

s = ding.Ding(
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

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.RetryAuthenticationRequest](../../models/components/retryauthenticationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.RetryResponse](../../models/operations/retryresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |

## send

Create an authentication

### Example Usage

```python
import ding
from ding.models import components

s = ding.Ding(
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    customer_uuid='82779012-9667-4917-8532-b94017ce3f0f',
    phone_number='+1234567890',
)

res = s.otp.send(req)

if res.create_authentication_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.CreateAuthenticationRequest](../../models/components/createauthenticationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateAutenticationResponse](../../models/operations/createautenticationresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |
