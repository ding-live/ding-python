"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import retryauthenticationresponse as components_retryauthenticationresponse
from typing import Optional


@dataclasses.dataclass
class RetryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    retry_authentication_response: Optional[components_retryauthenticationresponse.RetryAuthenticationResponse] = dataclasses.field(default=None)
    r"""OK"""
    
