"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import lookuprequest as components_lookuprequest
from ...models.components import lookupresponse as components_lookupresponse
from typing import Optional


@dataclasses.dataclass
class LookupRequest:
    customer_uuid: str = dataclasses.field(metadata={'header': { 'field_name': 'customer-uuid', 'style': 'simple', 'explode': False }})
    lookup_request: Optional[components_lookuprequest.LookupRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class LookupResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    lookup_response: Optional[components_lookupresponse.LookupResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
