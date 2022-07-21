import json, logging, requests

class Resellme:
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    API_ENDPOINT = "https://api.resellme.co.zw/api/"
    NAME_SERVER1 = "ns1.pnrhost.com"  # default resellme nameserver 1
    NAME_SERVER2 = "ns2.pnrhost.com"  # default resellme nameserver 2


    def __init__(self, api_key=""):
        """
        Instantiate a new Resellme object with the api_key provided
        """

        if not bool(api_key and not api_key.isspace()):
            raise ValueError("API Key cannot be empty")

        self.api_key = api_key
        self.headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": "Bearer {}".format(self.api_key),
        }

        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.company = ""
        self.mobile = ""
        self.street_address = ""
        self.core_business = ""
        self.city = ""
        self.country = ""
        self.domain_id = None


    def search_domain(self, domain: str):
        """
        Search a domain for availability
        """

        url = self.API_ENDPOINT + "v2/searches/"
        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")
        payload = json.dumps({"domain": domain})
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()


    def create_domain(self, domain: str):
        '''
        Creates the domain
        '''

        url = self.API_ENDPOINT + "v2/domains/"
        if not bool(domain and not domain.isspace()):
            raise ValueError("domain name cannot be empty")
        payload = json.dumps({"name": domain})
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()

    def register_domain(
        self,
        domain_name,
        email,
        first_name,
        last_name,
        company,
        mobile,
        street_address,
        core_business,
        city,
        country,
    ):

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

        domain_search_status = self.search_domain(domain_name)
        if domain_search_status["status"] == "available":
            domain_id = self.create_domain(domain_name)["id"]
            self.create_nameserver(domain_id)  # search the domain
            self.create_contact(domain_id)  # create the contact for the domain
            url = self.API_ENDPOINT + f"v1/domains/{domain_id}/register"

            payload = json.dumps(
                {
                    "domain_name": domain_name,
                    "email": self.email,
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "company": self.company,
                    "mobile": self.mobile,
                    "street_address": self.street_address,
                    "core_business": self.core_business,
                    "city": self.city,
                    "country": self.country,
                }
            )
            
            try:
                response = requests.request(
                    "POST", url, headers=self.headers, data=payload
                )
            except Exception as e:
                raise e
            return response.json()
        else:
            return json.dumps(domain_search_status)

    # def transfer_domain(self, **kwargs):
    #     url = self.API_ENDPOINT + "domains/2342/transfer"
    #     payload = json.dumps({**kwargs})
    #     try:
    #         response = requests.request("POST", url, headers=self.headers, data=payload)
    #     except Exception as e:
    #         raise e
    #     return response.text

    def get_domain_by_name(self, domain):
        """
        Get all the named domain
        """
        url = self.API_ENDPOINT + f"v1/domains?filter[name]={domain}"

        payload = json.dumps({})
        try:
            response = requests.request("GET", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()

    def get_all_domains(self):
        '''
        Returns all the doamins for the specified reseller
        '''

        url = self.API_ENDPOINT + 'v1/domains'

        payload = json.dumps({'status':'registered'})
        try:
            response = requests.request("GET", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()

    # def get_domain_extension_prices():
    #     url = self.API_ENDPOINT + "/extension-prices?include=currency,extension"
    #     payload = json.dumps()
    #     try:
    #         response = requests.request("GET", url, headers=self.headers, data=payload)
    #     except Exception as e:
    #         raise e
    #     return response.text

    # def renew_domain(self, domain):
    #     url = self.API_ENDPOINT + "/domains/242/renew"
    #     payload = json.dumps({"domain": domain})
    #     try:
    #         response = requests.request("POST", url, headers=self.headers, data=payload)
    #     except Exception as e:
    #         raise e
    #     return response.text

    def create_contact(self, domain_id):
        """
        Creates the contact details of the registering domain owner
        """
        url = self.API_ENDPOINT + "v2/contacts/"

        payload = json.dumps(
            {
                "domain_id": domain_id,
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "company": self.company,
                "mobile": self.mobile,
                "street_address": self.street_address,
                "core_business": self.core_business,
                "city": self.city,
                "country": self.country,
            }
        )

        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()


    def get_contact(self, contact_id):
        url = self.API_ENDPOINT + f"v1/contacts/{contact_id}"

        if not bool(contact_id and not contact_id.isspace()):
            raise ValueError("contact_id name cannot be empty")

        payload={}
        try:
            response = requests.request("GET", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()


    def update_contact(self, domain, email,first_name=None, 
                       last_name=None,
                       company=None,
                       mobile=None,
                       street_address=None,
                       core_business=None,
                       city=None,
                       country=None,
                       ):
        """
        Updates the contact details for the specified domain
        """

        contact_id =self.get_domain_by_name(domain)['data'][0]['relationships']['contact']['data']['id']
        old_contact_details = self.get_contact(contact_id)['data']['attributes']

        if not first_name:
            first_name = old_contact_details['first_name']
        if not last_name:
            last_name = old_contact_details['last_name']
        if not company:
            company = old_contact_details['company']
        if not mobile:
            mobile = old_contact_details['mobile']
        if not street_address:
            street_address = old_contact_details['street_address']
        if not core_business:
            core_business = old_contact_details['core_business']
        if not city:
            city = old_contact_details['city']
        if not country:
            country = old_contact_details['country']



        url = self.API_ENDPOINT + f"v1/contacts/{contact_id}"

        payload = json.dumps({
          "data": {
            "type": "contacts",
            "id": contact_id,
            "attributes": {
              "email": email,
              "first_name": first_name,
              "last_name": last_name,
              "company": company,
              "mobile": mobile,
              "street_address": street_address,
              "core_business": core_business,
              "city": city,
              "country": country,
            }
          }
        })
        try:
            response = requests.request("PATCH", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()

    def create_nameserver(self, domain_id, ns1=None, ns2=None):
        """
        Creates or updates the Resellme nameservers
        """

        url = self.API_ENDPOINT + "v1/nameservers"

        if ns1 and ns2:
            self.NAME_SERVER1 = ns1
            self.NAME_SERVER2 = ns2

        payload = json.dumps(
            {
                "data": {
                    "type": "nameservers",
                    "attributes": {
                        "domain_id": domain_id,
                        "ns1": self.NAME_SERVER1,
                        "ns2": self.NAME_SERVER2
                    }
                }
            }
        )
        try:
            response = requests.request("POST", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()


    def update_nameserver(self, domain, ns1='', ns2=''):
        """
        Creates or updates the Resellme nameservers
        """

        # get the ID of the nameserver specific to the domain
        nameserver_id =self.get_domain_by_name(domain)['data'][0]['relationships']['nameserver']['data']['id']
        url = self.API_ENDPOINT + f"v1/nameservers/{nameserver_id}"

        payload = json.dumps(
            {
                "data": {
                    "type": "nameservers",
                    "id": nameserver_id,
                    "attributes": {
                        "ns1": ns1,
                        "ns2": ns2
                    }
                }
            }
        )
        try:
            response = requests.request("PATCH", url, headers=self.headers, data=payload)
        except Exception as e:
            raise e
        return response.json()
