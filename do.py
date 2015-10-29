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

    def get_domain(self, domain):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        if domain is None:
            return "Please supply a domain. Ex. example.com"
        else:
            domain_url = base_url + 'domains/' + domain + ''
            domain_info = requests.get(domain_url, headers = token).json()
            if requests.get(domain_url, headers = token).status_code == 200:
                return domain_info
            else:
                return "Unable to find domain information for %s" % domain

    def domain_records(self, domain):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        records_url = base_url + 'domains/' + domain + '/records'
        records = requests.get(records_url, headers = token).json()
        if requests.get(records_url, headers = token).status_code == 200:
            return records
        else:
            return "Unable to fetch domain records. Check authorization token"

    def get_domain_record(self, id):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        if id is None:
            return "Please supply a domain record id."
        else:
            records_url = base_url + 'domains/' + domain + '/records/' + id + ''
            record = requests.get(records_url, headers = token).json()
            if record.status_code == 200:
                return records
            else:
                return "Unable to find supplied domain record id"