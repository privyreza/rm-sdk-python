import requests, json

class Resellme:

    hostname = 'http://127.0.0.1:8000/api/v1'

    def __init__(self, api_key=''):
        """ Instantiate a Resellme object """

        self.api_key = api_key
        self.domain_name = None
        self.headers = {"Accept": "application/vnd.api+json",
                          "Content-Type": "application/vnd.api+json",
                          "Authorization": "Bearer {}".format(self.api_key)

                        }


    def search_domain(self, domain_name):
        """ Method to search a domain before registration """

        self.domain_name = domain_name # sets the domain name
        data = { "domain" : self.domain_name}
        try:
            request = requests.post(self.hostname + "/searches", json.dumps(data), headers = self.headers)
            print(request.json())
        except Exception as e:
            print(e)


    def register_domain(self, domain_name):
        """ Method to register a /domains + domain id + /register """
        pass



resellme = Resellme(api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiYzdhZTkzOTQxZDViMWUyODVjMTBhOTdjZmJiOTI0ODU4ZmNhNmJlYjcwODdiNDdiN2U2MDUxMDU0N2YxNmVjNTNmNWQ0YTUzZjBjY2U5ODUiLCJpYXQiOjE2MjMzNDkwMDYuMTkzNjA3LCJuYmYiOjE2MjMzNDkwMDYuMTkzNjE3LCJleHAiOjE2NTQ4ODUwMDUuNDMzNjMsInN1YiI6IjMxIiwic2NvcGVzIjpbXX0.XKYBvp4YE50LWFq38g00xLLl8j0BD-l4IgUOXYtnjh2gqqQ7J8hHZSM01AB_6hQ-xrXze2zA6A1RY_fvSXJKBlls0zxdnv-uoUIWtoCQvSX08d3wWiO_-rin5989eqJwi78hrrqc9a0eHfte6nZhD4-eEVv6SzemJ7_5Tic5pcEL7-18-Up5v6_ow9awGvcr8TbrPEyAjp5d1RgOcALoWdg1jmU7Ji9XnPD4NRThHstxRXfQEaPMvRsFvEjPzCfSFNQdPv3KL2AHl53JDiG8XGD2TcEJv-SLiafSZsiReINNzOyTfI2M4j0Yleu17aMol9q5cwnTCoTfvQfd1co3KS3qHF40bcbLTcie5fwuAos2EtULdspzASeAWr4aDVNPchrymWq9MNf_l_cDOVBbXChll-0jPdhF1ncc_4fdaLZN4aj2Tosm36W_ntS0xz_bezugyk4rOLWu8ji9sX7XIs1dtsUKYO-GGq_tihj3CTQ-L1lSew32ST_-sRvX_MVUVmH_HAyjx31ibdypqzTqGSs9YSZ9VqsLpZ1UAUlZ6f5wmjZfl75ruVp1emZoPrhSPG8kfhGNMqXiyyU_Uv_Ow0bPHw89kRpTgw4Wh5wEy58LxWSkcFyAnt8kO05_o0zD5knJ6WKiq31ioVSAUUFoia5N_W7tFdNK_00TrfMKCB4')

resellme.search_domain('name.co.zw')
