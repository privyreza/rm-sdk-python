import requests


class Resellme:

    version = 'v1'
    base_url = 'https://api.resellme.co.zw/'
    registration_link = '/domain/'
    api_url = base_url + '/api/' + version

    def __init__(self):
        pass

    def register_domain(self, data):
        self.data = data
        return self.data

    def create_domain(self):
        pass

    def create_nameserver(self):
        pass

    def create_contact(self):
        pass
