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
    customer_uuid='c9f826e0-deca-41ec-871f-ecd6e8efeb46',
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
    customer_uuid='e0e7b0e9-739d-424b-922f-1c2cb48ab077',
    authentication_uuid='8f1196d5-806e-4b71-9b24-5f96ec052808',
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
    customer_uuid='c0c405fa-6bcb-4094-9430-7d6e2428ff23',
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