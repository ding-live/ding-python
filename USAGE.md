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