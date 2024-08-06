"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from ding import utils
from enum import Enum
from typing import Optional


class Status(str, Enum):
    r"""The status of the authentication. Possible values are:
      * `pending` - The OTP code is being sent.
      * `rate_limited` - This user is rate-limited and cannot receive another code.
      * `spam_detected` - This attempt is flagged as spam. Go to the dashboard for more details.
    """
    PENDING = 'pending'
    RATE_LIMITED = 'rate_limited'
    SPAM_DETECTED = 'spam_detected'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAuthenticationResponse:
    r"""A successful response to an authentication creation request."""
    authentication_uuid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authentication_uuid'), 'exclude': lambda f: f is None }})
    r"""A unique identifier for the authentication that you can use on the /check and /retry endpoints."""
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the authentication. Possible values are:
      * `pending` - The OTP code is being sent.
      * `rate_limited` - This user is rate-limited and cannot receive another code.
      * `spam_detected` - This attempt is flagged as spam. Go to the dashboard for more details.
    """
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The time at which the authentication expires and can no longer be checked or retried."""
    

