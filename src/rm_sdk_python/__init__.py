import requests, json


class Resellme:

    hostname = "https://api.resellme.co.zw/api/v1"

    def __init__(self, api_key=""):
        """ Instantiate a Resellme object """

        self.api_key = api_key
        self.domain_name = None
        self.headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": "Bearer {}".format(self.api_key),
        }

    def search_domain(self, domain_name):
        """ Method to search a domain before registration """

        self.domain_name = domain_name  # sets the domain name
        data = {"domain": self.domain_name}
        try:
            request = requests.post(
                self.hostname + "/searches", data=json.dumps(data), headers=self.headers
            )
            return request.json()
        except Exception as e:
            return

    def register_domain(self):
        """ Method to register a /domains + domain id + /register """
        print(self.domain_name)
