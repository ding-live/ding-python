<!-- Start SDK Example Usage [usage] -->
### Send a code

Send an OTP code to a user's phone number.


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

### Check a code

Check that a code entered by a user is valid.


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
    customer_uuid='cc0f6c04-40de-448f-8301-3cb0e6565dff',
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


res = s.lookup.lookup(phone_number='<value>', customer_uuid='69a197d9-356c-45d1-a807-41874e16b555')

if res.lookup_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->