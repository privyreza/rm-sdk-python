import json, logging, requests

# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

class Resellme:
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    API_ENDPOINT = "https://api.resellme.co.zw/api/v1"
    NAME_SERVER1 = "ns1.pnrhost.com"  # default resellme nameserver 1
    NAME_SERVER2 = "ns2.pnrhost.com"  # default resellme nameserver 2
    domain_id = ""  # domain id
    domain = ""  # domain name
    status = ""  # domain name

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



    def search_domain(self, domain:str) -> str:
        url = self.API_ENDPOINT + '/searches/'
        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")
        payload = json.dumps({"domain": domain})
        try:
            response = requests.requests("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def create_domain(self, domain:str) -> str:
        url = self.API_ENDPOINT + '/domains/'
        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")
        payload = json.dumps({"name": domain})
        try:
            response = requests.requests("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def register_domain(self, **kwargs) -> str:
        url = self.API_ENDPOINT + '/domains/{domain_id}/register'
        payload = json.dumps({**kwargs})
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def transfer_domain(self, **kwargs) -> str:
        url = self.API_ENDPOINT + '/domains/2342/transfer'
        payload = json.dumps({**kwargs})
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def get_domain() -> str:
        url = self.API_ENDPOINT + '/api/v1/domains'
        payload = json.dumps()
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def get_domain_extension_prices() -> str:
        url = self.API_ENDPOINT + '/extension-prices?include=currency,extension'
        payload = json.dumps()
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def renew_domain(self, domain) -> str:
        url = self.API_ENDPOINT + '/domains/242/renew'
        payload = json.dumps({'domain': domain})
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def create_contact(self, email, first_name, last_name, company, mobile, street_address,core_business,city,country) -> str:
        url = self.API_ENDPOINT + '/contacts/'

        payload = json.dumps({
          "domain_id": self.domain_id,
          "email": email,
          "first_name": first_name,
          "last_name": last_name,
          "company": company,
          "mobile": mobile,
          "street_address": street_address,
          "core_business": core_business,
          "city": city,
          "country": country
        })

        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text

    def create_nameserver() -> str:
        url = self.API_ENDPOINT + '/nameservers'

        payload = json.dumps({
          "data": {
            "type": "nameservers",
            "attributes": {
              "domain_id": self.domain_id,
              "ns1": self.NAME_SERVER1,
              "ns2": self.NAME_SERVER2,
            }
          }
        })

        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except Exception as e:
            raise e
        return response.text
