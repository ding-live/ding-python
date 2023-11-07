"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RetryAuthenticationRequest:
    authentication_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authentication_uuid') }})
    r"""The authentication UUID that was returned when you created the authentication."""
    customer_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_uuid') }})
    r"""Your customer UUID, which can be found in the API settings in the dashboard."""
    

