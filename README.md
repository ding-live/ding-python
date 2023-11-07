# Ding's Python SDK

## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:

- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install ding_sdk
```
<!-- End SDK Installation -->

## SDK Example Usage

<!-- Start SDK Example Usage -->
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [.otp](docs/sdks/otp/README.md)

* [post_authentication](docs/sdks/otp/README.md#post_authentication) - Create an authentication
* [post_check](docs/sdks/otp/README.md#post_check) - Check an authentication code
* [post_retry](docs/sdks/otp/README.md#post_retry) - Retry an authentication

### [.lookup](docs/sdks/lookup/README.md)

* [post_lookup](docs/sdks/lookup/README.md#post_lookup) - Lookup a phone number
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


## Example

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

res = None
try:
    res = s.otp.post_authentication(req)

except (ErrorResponse) as e:
    print(e) # handle exception


if res.create_authentication_response is not None:
    # handle response
    pass
```
<!-- End Error Handling -->

<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.ding.live/v1` | None |

For example:

```python
import ding
from ding.models import shared

s = ding.Ding(
    server_idx=0,
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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import ding
from ding.models import shared

s = ding.Ding(
    server_url="https://api.ding.live/v1",
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
<!-- End Server Selection -->

<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import ding
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = ding.Ding(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Start Authentication -->
# Authentication

## Per-Client Security Schemes

Your SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:

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
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
