import json, logging, requests


class Resellme:
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    API_ENDPOINT = "https://api.resellme.co.zw/api/v1"
    NAME_SERVER1 = "ns1.cloud-dns.com"  # default resellme nameserver 1
    NAME_SERVER2 = "ns2.cloud-dns.com"  # default resellme nameserver 2

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
                self.API_ENDPOINT + "/searches",
                data=json.dumps(data),
                headers=self.headers,
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

    def register_domain(
        self,
        domain_name="",
        first_name="",
        last_name="",
        email="",
        company="",
        mobile="",
        street_address="",
        core_business="",
        city="",
        country="",
        name_server1=None,
        name_server2=None,
    ):

        """ Method to register a /domains + domain id + /register """

        # TODO: Check user nameservers

        if (name_server1 == None) and (name_server2 == None):
            name_server1 = self.NAME_SERVER1
            name_server2 = self.NAME_SERVER2

        nameservers = {"ns1": name_server1, "ns2": name_server2}

        # first lets search if the domain is available

        if (
            domain_name
            and first_name
            and last_name
            and email
            and company
            and mobile
            and street_address
            and core_business
            and city
            and country
        ):
            results = self.search_domain(domain_name)

            # TODO: check with server of valid responses

            if results["status"] == "pending":

                domain_id = results.get(
                    "id", None
                )  # TODO: way to check if its none may throw error

                contacts = {
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
                        "domain_id": domain_id,  # get from search
                    }
                }

                data = {
                    "domain": domain_name,
                    "nameservers": nameservers,
                    "contacts": contacts,
                }
                try:

                    print(json.dumps(data))

                    resp = requests.post(
                        self.API_ENDPOINT + "/domains/{}/register".format(domain_id),
                        data=json.dumps(data),
                        headers=self.headers,
                    )
                    return resp.json()
                except Exception as e:
                    self.log.error("Something went wrong:", e)
            else:
                raise ValueError("The domain {} is not available ".format(domain_name))

        def get_domain(self):
            pass


# resellme = Resellme(api_key='')
# print(resellme.search_domain('xyz.co.zw'))
# print(resellme.register_domain(
#     domain_name='xbc.co.zw',
#     first_name='test1',
#     last_name='test1',
#     email='test1@test1.com',
#     company='test1',
#     mobile='0777054115',
#     street_address='test1',
#     core_business='test1',
#     city='Harare',
#     country='Zimbabwe',
# ))
