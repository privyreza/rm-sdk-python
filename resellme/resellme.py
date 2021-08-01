import requests

class Resellme:

    hostname = 'https://api.resellme.co.zw/api/v1'

    def __init__(self, api_key=''):
        """ Instantiate a Resellme object """

        self.api_key = api_key
        self.domain_name = None
        self.headers = { "Accept": "application/vnd.api+json",
                          "Content-Type": "application/vnd.api+json",
                          "Authorization": "Bearer {}".format(self.api_key)

                        }


    def search_domain(self, domain_name):
        """ Method to search a domain before registration """

        self.domain_name = domain_name # sets the domain name
        data = { "domain" : self.domain_name}
        with requests.Session() as s:
            try:
                request = s.post(self.hostname + "/searches", data=data, headers = self.headers)
                print(request.text)
            except Exception as e:
                print(e)


    def register_domain(self, domain_name):
        """ Method to register a /domains + domain id + /register """
        pass



resellme = Resellme(api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3IiwianRpIjoiMzQ1OGUzMThjYTg1ODA2MzZiZDkxZDYwNWY0ZTMxN2RiNWI0MmE5OTA0ZTYzZTlhYjJkZGMxYTI5MmI1MjQ5OGE3MGEyMmQ1MmE2OWMyMmYiLCJpYXQiOjE2Mjc4MjI5MjYuNjk4ODMzLCJuYmYiOjE2Mjc4MjI5MjYuNjk4ODM2LCJleHAiOjE2NTkzNTg5MjYuNjkxNjA0LCJzdWIiOiIyOTUiLCJzY29wZXMiOltdfQ.e5MH1D_ovuKxqzNtJzxnNrIJ5mBMaechItu7YfNiczAz3nR_POWDWdSxPEwgN4YgscnmnEaPgKFrxM6qVS3lNU6DeZj8-gybVsx2VccbCzoINfss-7-Q661px7hoCE1D4aNX0OnyTOmVW8rp2Ut_6E26AsMa6Si59upsQRkZFiLe6sgesl42B3Dk74p3qFeIm0uu53THgbwLIYxBXWMLQzj0g_RPKzQQCMSClicZKa-6fa6k-sWV6zkLHkuTXKZ4hOK2xE4jrLwd6EAytJehZf_JKK6qwrVIW9tWun21pwxVChxyFcrfx8SxUD9Z6-XKDXp4lJAMAU7GukYRlYXWg1itruXuxkk2dk1r8tklxuiWYmf9PKmVaUinlu12ri_0d_JwJ-uixJdcICn1hR5RuJGGG7zebllXNnKQPAOhpxSvuqUqiJVfMBJmfpTKhU1xPXLE7hCRaWMntmshEOciszYdgqjjFCUJaJ7NE51TJdAqGTaQwTTeZylfvAU5bdjCAIbYaQDrJ7tWKniC8y6UjbOSkNzDiG3Xmv7p7b8T7pKOvAdWcin5AFZacMkiaubY6_8qmR5GlDpTikLixuBVKZN7xrrBf14LpVGi588WtJTgnjcDFa1B2ZUUI2Tjarj-CwyvS6ZLzkXovIuYBDyP0xPls-gVR6q3l2gQTXANKZs')

resellme.search_domain('fake.co.zw')
