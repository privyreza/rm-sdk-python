import json, logging, requests
import jsonapi_requests

# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

class Resellme:
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    API_ENDPOINT = "https://api.resellme.co.zw/api/v1"
    NAME_SERVER1 = "cloud-ns1.pnrhost.com"  # default resellme nameserver 1
    NAME_SERVER2 = "cloud-ns2.pnrhost.com"  # default resellme nameserver 2
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

    def search_domain(self, domain):
        """ Method to search a domain before registration """

        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")

        # TODO: Sanitize URL from users
        self.domain = domain

 
        data = {"domain": self.domain}
        try:
            request = requests.post(
                self.API_ENDPOINT + "/searches",
                data=json.dumps(data),
                headers=self.headers,
                # proxies=proxies,
                # verify=False,
            )
            self.domain_id = request.json()["id"]
            self.status = request.json()["status"]
            return request.json()
        except Exception as e:
            self.log.error("Error Occurred: {}".format(e))

    def createNS(self, data):

        try:
            resp = requests.post(
                self.API_ENDPOINT + "/nameservers/",
                data=json.dumps(data),
                headers=self.headers,
                # proxies=proxies,
                # verify=False,
            )
            return resp.json()
        except Exception as e:
            self.log.error("Error Occurred: {}".format(e))

    def create_contact(self, data):
        try:
            resp = requests.post(
                self.API_ENDPOINT + "/contacts/",
                data=json.dumps(data),
                headers=self.headers,
                # proxies=proxies,
                # verify=False,
            )
            return resp.json()
        except Exception as e:
            self.log.error("Error Occurred: {}".format(e))

    def register_domain(
        self,
        first_name='',
        last_name='',
        email='',
        company='',
        mobile='',
        street_address='',
        core_business='',
        city='',
        country='',
        ns1=None,
        ns2=None,
    ):

        """ Method to register a domain at this endpoint /domains + domain id + /register """

        if ns1 and ns2:
            self.NAME_SERVER1 = ns1
            self.NAME_SERVER2 = ns2
        if self.status == 'pending':

            nameservers = {
                "data": {
                    "type": "nameservers",
                    "attributes": {
                        "ns1": self.NAME_SERVER1,
                        "ns2": self.NAME_SERVER2,
                        "domain_id": self.domain_id,
                    },
                }
            }

            contacts = {
                "data": {
                    "type": "contacts",
                    "attributes": {
                        "registrant": {
                            "first_name": first_name,
                            "last_name": last_name,
                            "email": email,
                            "company": company,
                            "mobile": mobile,
                            "street_address": street_address,
                            "core_business": core_business,
                            "city": city,
                            "country": country,
                            "domain_id": self.domain_id,
                        }
                    },
                }
            }

            self.createNS(nameservers)
            self.create_contact(contacts)

            data = {
                "data": {
                    "type": "data",
                    "attributes": {
                        "domain": self.domain_id,
                        "nameservers": nameservers,
                        "contacts": contacts,
                    },
                }
            }



            try:
                resp = requests.post(
                    self.API_ENDPOINT + "/domains/" + str(self.domain_id) + "/register",
                    data=json.dumps(data),
                    headers=self.headers,
                    # proxies=proxies,
                    # verify=False,
                )
                return resp.json()
            except Exception as e:
                self.log.error("Error Occurred: {}".format(e))
        else:
            raise ValueError('Domain not available')


# resellme = Resellme(
#     api_key=""
# )
# print(resellme.search_domain("omg123456.co.zw"))

# print(
#     resellme.register_domain(
#         first_name='tested',
#         last_name='tested',
#         email='tested',
#         company='tested',
#         mobile='tested',
#         street_address='tested',
#         core_business='tested',
#         city='tested',
#         country='tested',
#     )
# )
