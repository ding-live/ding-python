<!-- Start SDK Example Usage -->

## Send a code
This example shows how to send an OTP code to a user's phone number.

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
<!-- End SDK Example Usage -->