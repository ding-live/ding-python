"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import authenticationstatusresponse as components_authenticationstatusresponse
from typing import Optional


@dataclasses.dataclass
class GetAuthenticationStatusRequest:
    auth_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'auth_uuid', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetAuthenticationStatusResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    authentication_status_response: Optional[components_authenticationstatusresponse.AuthenticationStatusResponse] = dataclasses.field(default=None)
    r"""OK"""
    

