<!-- Start SDK Example Usage [usage] -->
### Send a code

Send an OTP code to a user's phone number.


```python
import ding
from ding.models import components

s = ding.Ding(
    api_key="YOUR_API_KEY",
)


res = s.otp.create_authentication(request=components.CreateAuthenticationRequest(
    customer_uuid='c9f826e0-deca-41ec-871f-ecd6e8efeb46',
    phone_number='+1234567890',
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
    api_key="YOUR_API_KEY",
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
    api_key="YOUR_API_KEY",
)


res = s.otp.retry()

if res.retry_authentication_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->