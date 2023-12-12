"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from ding import utils
from enum import Enum
from typing import Optional

class Code(str, Enum):
    r"""A machine-readable code that describes the error. Possible values are:
      * `invalid_phone_number` - This is not a valid E.164 number.
      * `internal_server_error` - An internal server error occurred.
      * `bad_request` - The request was malformed.
      * `account_invalid` - The provided customer UUID is invalid.
      * `negative_balance` - You have a negative balance.
      * `invalid_line` - Ding does not support this type of phone number.
      * `unsupported_region` - Ding does not support this region yet.
      * `invalid_auth_uuid` - The provided authentication UUID is invalid.
      * `blocked_number` - The phone number is in the blocklist.
      * `invalid_app_version` - The provided application version is invalid.
      * `invalid_os_version` - The provided OS version is invalid.
      * `invalid_device_model` - The provided device model is invalid.
      * `invalid_device_id` - The provided device ID is invalid.
    """
    INVALID_PHONE_NUMBER = 'invalid_phone_number'
    INTERNAL_SERVER_ERROR = 'internal_server_error'
    BAD_REQUEST = 'bad_request'
    ACCOUNT_INVALID = 'account_invalid'
    NEGATIVE_BALANCE = 'negative_balance'
    INVALID_LINE = 'invalid_line'
    UNSUPPORTED_REGION = 'unsupported_region'
    INVALID_AUTH_UUID = 'invalid_auth_uuid'
    INVALID_APP_REALM = 'invalid_app_realm'
    UNSUPPORTED_APP_REALM_DEVICE_TYPE = 'unsupported_app_realm_device_type'
    APP_REALM_REQUIRE_DEVICE_TYPE = 'app_realm_require_device_type'
    BLOCKED_NUMBER = 'blocked_number'
    INVALID_APP_VERSION = 'invalid_app_version'
    INVALID_OS_VERSION = 'invalid_os_version'
    INVALID_DEVICE_MODEL = 'invalid_device_model'
    INVALID_DEVICE_ID = 'invalid_device_id'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ErrorResponse(Exception):
    r"""Bad Request"""
    code: Optional[Code] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""A machine-readable code that describes the error. Possible values are:
      * `invalid_phone_number` - This is not a valid E.164 number.
      * `internal_server_error` - An internal server error occurred.
      * `bad_request` - The request was malformed.
      * `account_invalid` - The provided customer UUID is invalid.
      * `negative_balance` - You have a negative balance.
      * `invalid_line` - Ding does not support this type of phone number.
      * `unsupported_region` - Ding does not support this region yet.
      * `invalid_auth_uuid` - The provided authentication UUID is invalid.
      * `blocked_number` - The phone number is in the blocklist.
      * `invalid_app_version` - The provided application version is invalid.
      * `invalid_os_version` - The provided OS version is invalid.
      * `invalid_device_model` - The provided device model is invalid.
      * `invalid_device_id` - The provided device ID is invalid.
    """
    doc_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doc_url'), 'exclude': lambda f: f is None }})
    r"""A link to the documentation that describes the error."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""A human-readable message that describes the error."""
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
