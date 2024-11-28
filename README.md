# Ding Python SDK

The Ding Python library provides convenient access to the Ding API from applications written in the Python language.

<!-- Start Summary [summary] -->
## Summary

Ding: The OTP API allows you to send authentication codes to your users using their phone numbers.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Ding Python SDK](#ding-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [SDK Example Usage](#sdk-example-usage-1)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
* [Development](#development)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed using the *pip* package manager, with dependencies and metadata stored in the `setup.py` file.

```bash
pip install ding_api_client
```
<!-- End SDK Installation [installation] -->

## SDK Example Usage

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Send a code

Send an OTP code to a user's phone number.


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

### Check a code

Check that a code entered by a user is valid.


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

### Perform a retry

Perform a retry if a user has not received the code.


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

### Send feedback

Send feedback about the authentication process.


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

### Get authentication status

Get the status of an authentication.


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

### Look up for phone number

Perform a phone number lookup.


```python
import ding

s = ding.Ding(
    api_key='YOUR_API_KEY',
)


res = s.lookup.lookup(phone_number='<value>', customer_uuid='6e93aa15-9177-4d09-8395-b69ce50db1c8')

if res.lookup_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [lookup](docs/sdks/lookup/README.md)

* [lookup](docs/sdks/lookup/README.md#lookup) - Look up for phone number

### [otp](docs/sdks/otp/README.md)

* [create_authentication](docs/sdks/otp/README.md#create_authentication) - Send a code
* [check](docs/sdks/otp/README.md#check) - Check a code
* [feedback](docs/sdks/otp/README.md#feedback) - Send feedback
* [get_authentication_status](docs/sdks/otp/README.md#get_authentication_status) - Get authentication status
* [retry](docs/sdks/otp/README.md#retry) - Perform a retry

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exception. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_authentication` method may raise the following exceptions:

| Error Type           | Status Code | Content Type     |
| -------------------- | ----------- | ---------------- |
| errors.ErrorResponse | 400         | application/json |
| errors.SDKError      | 4XX, 5XX    | \*/\*            |

### Example

```python
import ding
from ding.models import components, errors

s = ding.Ding(
    api_key='YOUR_API_KEY',
)

res = None
try:
    res = s.otp.create_authentication(request=components.CreateAuthenticationRequest(
    customer_uuid='c9f826e0-deca-41ec-871f-ecd6e8efeb46',
    phone_number='+1234567890',
    locale='fr-FR',
))

except errors.ErrorResponse as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.create_authentication_response is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import ding
from ding.models import components

s = ding.Ding(
    server_url='https://api.ding.live/v1',
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import ding
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = ding.Ding(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type   | Scheme  |
| --------- | ------ | ------- |
| `api_key` | apiKey | API key |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!
