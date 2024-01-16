"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple, Callable, Union
from .utils.retries import RetryConfig
from .utils import utils
from ding.models import components


SERVER_PRODUCTION = 'production'
r"""The production Ding API server"""
SERVERS = {
	SERVER_PRODUCTION: 'https://api.ding.live/v1',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[components.Security,Callable[[], components.Security]] = None
    server_url: str = ''
    server: str = ''
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '1.3.2'
    gen_version: str = '2.233.2'
    user_agent: str = 'speakeasy-sdk/python 1.3.2 2.233.2 1.0.0 ding_api_client'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PRODUCTION

        return SERVERS[self.server], {}
