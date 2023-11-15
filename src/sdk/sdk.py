"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .lookup import Lookup
from .otp import Otp
from .sdkconfiguration import SDKConfiguration
from sdk import utils
from sdk.models import components
from typing import Callable, Dict, Union

class SDK:
    r"""Ding: The OTP API allows you to send authentication codes to your users using their phone numbers."""
    otp: Otp
    r"""Send OTP codes to your users using their phone numbers."""
    lookup: Lookup
    r"""Retrieve up-to-date metadata about a specific phone number"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key: Union[str,Callable[[], str]],
                 server: str = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param api_key: The api_key required for authentication
        :type api_key: Union[str,Callable[[], str]]
        :param server: The server by name to use for all operations
        :type server: str
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security = components.Security(api_key = api_key)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.otp = Otp(self.sdk_configuration)
        self.lookup = Lookup(self.sdk_configuration)
    