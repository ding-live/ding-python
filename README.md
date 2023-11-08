# ding_client_sdk

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/ding-live/ding-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/ding-live/ding-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation -->
# SDK Installation

```bash
pip install ding_client_sdk
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->

# Send a code
This example shows how to send an OTP code to a user's phone number.

```python
import ding
from ding.models import components

s = ding.Ding(
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
# Available Resources and Operations


## [.otp](docs/sdks/otp/README.md)

* [check](docs/sdks/otp/README.md#check) - Check an authentication code
* [create_autentication](docs/sdks/otp/README.md#create_autentication) - Create an authentication
* [retry](docs/sdks/otp/README.md#retry) - Retry an authentication

## [.lookup](docs/sdks/lookup/README.md)

* [lookup](docs/sdks/lookup/README.md#lookup) - Lookup a phone number
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->



<!-- End Dev Containers -->

<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |


## Example

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

res = None
try:
    res = s.otp.check(req)
except (errors.ErrorResponse) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.create_check_response is not None:
    # handle response
    pass
```
<!-- End Error Handling -->

<!-- Start Server Selection -->
# Server Selection

## Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `production` | `https://api.ding.live/v1` | None |

For example:

```python
import ding
from ding.models import components

s = ding.Ding(
    server="production",
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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import ding
from ding.models import components

s = ding.Ding(
    server_url="https://api.ding.live/v1",
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
