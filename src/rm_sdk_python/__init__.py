import json
import logging

import requests


class Resellme:
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    API_ENDPOINT = "https://api.resellme.co.zw/api/v1"

    def __init__(self, api_key=""):
        """ Instantiate a Resellme object """

        if not bool(api_key and not api_key.isspace()):
            raise ValueError("API Key cannot be empty")

        self.api_key = api_key
        self.headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": "Bearer {}".format(self.api_key),
        }

    def search_domain(self, domain_name):
        """ Method to search a domain before registration """

        if not bool(domain_name and not domain_name.isspace()):
            raise ValueError("domain name cannot be empty")

        data = {"domain": domain_name}
        try:
            request = requests.post(
                self.API_ENDPOINT + "/searches", data=json.dumps(data), headers=self.headers
            )
            return request.json()
        except requests.exceptions.HTTPError as http_error:
            self.log.error("Http Error:", http_error)
            raise http_error
        except requests.exceptions.ConnectionError as conn_error:
            self.log.error("Error Connecting:", conn_error)
            raise conn_error
        except requests.exceptions.Timeout as timeout_error:
            self.log.error("Timeout Error:", timeout_error)
            raise timeout_error
        except requests.exceptions.RequestException as err:
            self.log.error("Something went wrong:", err)
            raise err

    def register_domain(self):
        """ Method to register a /domains + domain id + /register """
        print(self.domain_name)
