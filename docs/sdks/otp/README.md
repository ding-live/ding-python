# Otp
(*otp*)

## Overview

Send OTP codes to your users using their phone numbers.

### Available Operations

* [create_authentication](#create_authentication) - Send a code
* [check](#check) - Check a code
* [feedback](#feedback) - Send feedback
* [get_authentication_status](#get_authentication_status) - Get authentication status
* [retry](#retry) - Perform a retry

## create_authentication

Send a code

### Example Usage

```python
import ding
from ding.models import components

s = ding.Ding(
    api_key='YOUR_API_KEY',
)


res = s.otp.create_authentication(request=components.CreateAuthenticationRequest(
    customer_uuid='cf2edc1c-7fc6-48fb-86da-b7508c6b7b71',
    phone_number='+1234567890',
    locale='fr-FR',
))

if res.create_authentication_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.CreateAuthenticationRequest](../../models/components/createauthenticationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |

### Response

**[operations.CreateAuthenticationResponse](../../models/operations/createauthenticationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## check

Check a code

### Example Usage

```python
import ding
from ding.models import components

s = ding.Ding(
    api_key='YOUR_API_KEY',
)


res = s.otp.check(request=components.CreateCheckRequest(
    customer_uuid='eebe792b-2fcc-44a0-87f1-650e79259e02',
    authentication_uuid='64f66a7c-4b2c-4131-a8ff-d5b954cca05f',
    check_code='123456',
))

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

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## feedback

Send feedback

### Example Usage

```python
import ding
from ding.models import components

s = ding.Ding(
    api_key='YOUR_API_KEY',
)


res = s.otp.feedback(request=components.FeedbackRequest(
    customer_uuid='cc0f6c04-40de-448f-8301-3cb0e6565dff',
    phone_number='+1234567890',
    status=components.FeedbackRequestStatus.ONBOARDED,
))

if res.feedback_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.FeedbackRequest](../../models/components/feedbackrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |

### Response

**[operations.FeedbackResponse](../../models/operations/feedbackresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## get_authentication_status

Get authentication status

### Example Usage

```python
import ding

s = ding.Ding(
    api_key='YOUR_API_KEY',
)


res = s.otp.get_authentication_status(auth_uuid='d8446450-f2fa-4dd9-806b-df5b8c661f23')

if res.authentication_status_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `auth_uuid`        | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetAuthenticationStatusResponse](../../models/operations/getauthenticationstatusresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## retry

Perform a retry

### Example Usage

```python
import ding

s = ding.Ding(
    api_key='YOUR_API_KEY',
)


res = s.otp.retry()

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

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |