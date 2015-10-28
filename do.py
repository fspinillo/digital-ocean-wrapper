import requests
import json

base_url = 'https://api.digitalocean.com/v2/'
header_type = "'Content-Type': 'application/json'"

class User(object):

    def __init__(self, token):
        self.token = token

    def account(self):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        account_url = base_url + 'account'
        account_info = requests.get(account_url, headers = token).json()

        return account_info

    def domains(self):
        domain_url = base_url + 'domains'
        header = {'Authorization': 'Bearer ' + self.token + '', 'Content-Type': 'application/json'}
        domains_list = requests.get(domain_url, headers = header).json()

        return domains_list