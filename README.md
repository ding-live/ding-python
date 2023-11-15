# openapi

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
## SDK Installation

```bash
pip install openapi
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Send a code

Send an OTP code to a user's phone number.


```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    customer_uuid='eae192ab-9e1e-4b21-b5b1-bfcb79a32fcc',
    phone_number='+1234567890',
)

res = s.otp.create_autentication(req)

if res.create_authentication_response is not None:
    # handle response
    pass
```

### Check a code

Check that a code entered by a user is valid.


```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="YOUR_API_KEY",
)

req = components.CreateCheckRequest(
    customer_uuid='e0e7b0e9-739d-424b-922f-1c2cb48ab077',
    authentication_uuid='8f1196d5-806e-4b71-9b24-5f96ec052808',
    check_code='123456',
)

res = s.otp.check(req)

if res.create_check_response is not None:
    # handle response
    pass
```

### Perform a retry

Perform a retry if a user has not received the code.


```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="YOUR_API_KEY",
)

req = components.RetryAuthenticationRequest(
    customer_uuid='a74ee547-564d-487a-91df-37fb25413a91',
    authentication_uuid='3c8b3a46-881e-4cdd-93a6-f7f238bf020a',
)

res = s.otp.retry(req)

if res.retry_authentication_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [otp](docs/sdks/otp/README.md)

* [create_autentication](docs/sdks/otp/README.md#create_autentication) - Send a code
* [check](docs/sdks/otp/README.md#check) - Check a code
* [retry](docs/sdks/otp/README.md#retry) - Perform a retry

### [lookup](docs/sdks/lookup/README.md)

* [lookup](docs/sdks/lookup/README.md#lookup) - Perform a phone number lookup
<!-- End SDK Available Operations -->

<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 400-600              | */*                  |

### Example

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    customer_uuid='eae192ab-9e1e-4b21-b5b1-bfcb79a32fcc',
    phone_number='+1234567890',
)

res = None
try:
    res = s.otp.create_autentication(req)
except (errors.ErrorResponse) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.create_authentication_response is not None:
    # handle response
    pass
```
<!-- End Error Handling -->

<!-- Start Server Selection -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `production` | `https://api.ding.live/v1` | None |
#### Example

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    server="production",
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    customer_uuid='eae192ab-9e1e-4b21-b5b1-bfcb79a32fcc',
    phone_number='+1234567890',
)

res = s.otp.create_autentication(req)

if res.create_authentication_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import sdk
from sdk.models import components

s = sdk.SDK(
    server_url="https://api.ding.live/v1",
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    customer_uuid='eae192ab-9e1e-4b21-b5b1-bfcb79a32fcc',
    phone_number='+1234567890',
)

res = s.otp.create_autentication(req)

if res.create_authentication_response is not None:
    # handle response
    pass
```
<!-- End Server Selection -->

<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Start Authentication -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import sdk
from sdk.models import components

s = sdk.SDK(
    api_key="YOUR_API_KEY",
)

req = components.CreateAuthenticationRequest(
    customer_uuid='eae192ab-9e1e-4b21-b5b1-bfcb79a32fcc',
    phone_number='+1234567890',
)

res = s.otp.create_autentication(req)

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
