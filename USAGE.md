<!-- Start SDK Example Usage -->

## Send a code
Send an OTP code to a user's phone number.

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


## Check a code
Check that a code entered by a user is valid.

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


## Retry an authentication
Retry an authentication if a user has not received the code.

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
<!-- End SDK Example Usage -->