import json, logging, requests

# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

class Resellme:
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    API_ENDPOINT = "https://api.resellme.co.zw/api/"
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

        self.email = ''
        self.first_name = ''
        self.last_name = ''
        self.company = ''
        self.mobile = ''
        self.street_address = ''
        self.core_business = ''
        self.city = ''
        self.country = ''


    def search_domain(self, domain:str) -> str:
        url = self.API_ENDPOINT + 'v1/searches/'
        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")
        payload = json.dumps({"domain": domain})
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()


    def create_domain(self, domain:str) -> str:
        url = self.API_ENDPOINT + 'v2/domains/'
        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")
        payload = json.dumps({"name": domain})
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text

    
    def register_domain(self, domain_name, email, first_name, last_name, company, mobile, street_address,core_business,city,country) -> str:

        self.domain_name = domain_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.mobile = mobile
        self.street_address = street_address
        self.core_business = core_business
        self.city = city
        self.country = country

        domain_id = self.search_domain(domain_name)['id']
        self.create_nameserver(domain_id)
        self.create_contact(domain_id)
        url = self.API_ENDPOINT + f'v1/domains/{domain_id}/register'

        payload = json.dumps({'domain_name': domain_name,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company': self.company,
            'mobile': self.mobile,
            'street_address': self.street_address,
            'core_business' : self.core_business,
            'city': self.city,
            'country': self.country
            })
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()


    def transfer_domain(self, **kwargs) -> str:
        url = self.API_ENDPOINT + '/domains/2342/transfer'
        payload = json.dumps({**kwargs})
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def get_domain() -> str:
        url = self.API_ENDPOINT + '/api/v1/domains'
        payload = json.dumps()
        try:
            response = requests.request("GET", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def get_domain_extension_prices() -> str:
        url = self.API_ENDPOINT + '/extension-prices?include=currency,extension'
        payload = json.dumps()
        try:
            response = requests.request("GET", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def renew_domain(self, domain) -> str:
        url = self.API_ENDPOINT + '/domains/242/renew'
        payload = json.dumps({'domain': domain})
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


    def create_contact(self, domain_id) -> str:
        url = self.API_ENDPOINT + 'v1/contacts/'

        payload = json.dumps({
          "domain_id": domain_id,
          "email": self.email,
          "first_name": self.first_name,
          "last_name": self.last_name,
          "company": self.company,
          "mobile": self.mobile,
          "street_address": self.street_address,
          "core_business": self.core_business,
          "city": self.city,
          "country": self.country
        })

        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()

    def create_nameserver(self, domain_id) -> str:
        url = self.API_ENDPOINT + 'v1/nameservers'

        payload = json.dumps({
          "data": {
            "type": "nameservers",
            "attributes": {
              "domain_id": domain_id,
              "ns1": self.NAME_SERVER1,
              "ns2": self.NAME_SERVER2,
            }
          }
        })

        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.text


resellme = Resellme(api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3IiwianRpIjoiMWFkYmQ1MmU0YjdkNWZiOTFkZTYxOGFkYjJiMDU5OTgzZmQ2NDM1ZTA1Yzc4NTE3NzcyOGVlODAzNDA5MmRkMWM0NWIxOGI5Yjg5OWYzOTYiLCJpYXQiOjE2NTgyNjY3MzAuMjE2NjcyLCJuYmYiOjE2NTgyNjY3MzAuMjE2Njc2LCJleHAiOjE2ODk4MDI3MzAuMjA4OTM3LCJzdWIiOiIyOTUiLCJzY29wZXMiOltdfQ.D7cMX7bSsWK_CLLD8QhzOHQUZzKwdGjS741onRTiLmCF9OhcNENM8NlAiR4zKJjr0dOw_rcQ7BkJvG6mclhCngsWhK8vBxuxi6CA6Mc9CA2Rdp_zmxRDiQcXQd3DOzqxl43AgNm8hU8QcIMYve3tMsU6vmiK3EsqvkrHM3GHFY26IaRza4xOjRgPOA7YwlJSObYuiXRFc9m3j5V4fqOIBDDAmrbBXqPfK1SvxAmVyJRwRomSLvzuA7VGQzOtiT6MFDTr-qBlJ4ZMmWIs51wa-F0xKc8jSvfQx1LJ7D30rdZJEKdgG95Ac9nxZ1oBpZj68PKOYrY7DDpoqDvNm-FoFHQoHWAJVW7mMVxU_Fvu9W9RSBx_MDmQBTlYTI0gr35u3hT9rQ1n5X9Kzk68g77J9qhrAYtIxyE-B9CSUR_qzgfHOfh8lbDOZ7WHPKx4FbzHibloBLt_rXYFyqI1Nms9922DJbN4ilEgYaESkeOJFbL4nXY0qdXISeRLRTFU9hWEiUUM5p1CEPn49XBldzvJ_UQoAcML9LaPq3QXYv8Iy9VV2a8svp87ddc1wvY44nhoyf6h-n7rG1YWHcEy1XnPoh9jHtw9ULe6aRr6UdHTZpNSW0dJJKuQWfJzxGNUzhXrAf4yeO3tuFoJBeI-KMUamCIxasipL9-PjDG3fnyqCzo')
# res = resellme.search_domain('test5.co.zw')
# res2 = resellme.create_domain('test2.co.zw')
# print(res)
# print(res2)

res3 = resellme.register_domain(
    domain_name='test4.co.zw',
    first_name='test1',
    last_name='test1',
    email='test1@test1.com',
    company='test1',
    mobile='0777054115',
    street_address='test1',
    core_business='test1',
    city='Harare',
    country='Zimbabwe',
)

print(res3)

