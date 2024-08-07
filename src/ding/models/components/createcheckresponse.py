"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from ding import utils
from enum import Enum
from typing import Optional


class CreateCheckResponseStatus(str, Enum):
    r"""The status of the check. Possible values are:
      * `valid` - The code is valid.
      * `invalid` - The code is invalid.
      * `without_attempt` - No attempt was sent yet, so a check cannot be completed.
      * `rate_limited` - The authentication was rate limited and cannot be checked.
      * `already_validated` - The authentication has already been validated.
      * `expired_auth` - The authentication has expired and cannot be checked.
    """
    VALID = 'valid'
    INVALID = 'invalid'
    WITHOUT_ATTEMPT = 'without_attempt'
    RATE_LIMITED = 'rate_limited'
    ALREADY_VALIDATED = 'already_validated'
    EXPIRED_AUTH = 'expired_auth'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateCheckResponse:
    authentication_uuid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authentication_uuid'), 'exclude': lambda f: f is None }})
    r"""The UUID of the corresponding authentication."""
    status: Optional[CreateCheckResponseStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the check. Possible values are:
      * `valid` - The code is valid.
      * `invalid` - The code is invalid.
      * `without_attempt` - No attempt was sent yet, so a check cannot be completed.
      * `rate_limited` - The authentication was rate limited and cannot be checked.
      * `already_validated` - The authentication has already been validated.
      * `expired_auth` - The authentication has expired and cannot be checked.
    """
    

