import requests
import json

base_url = 'https://api.digitalocean.com/v2'
header_type = "'Content-Type': 'application/json'"


def get(url, header, params=None):
    data = requests.get(url, headers = header)
    if data.status_code == 200:
        data = data.json()
    else:
        data = 'Unable to validate get request'

    return data


class User(object):

    def __init__(self, token):
        self.token = token
        self._account = '{BASE}/account'.format(BASE=base_url)
        self._domains = '{BASE}/domains/'.format(BASE=base_url)
        self._droplets = '{BASE}/droplets'.format(BASE=base_url)

    def account(self):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        account_info = get(self._account, header=token)

        return account_info

    def domains(self):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        domains_list = get(self._domains, header=token)

        return domains_list

    def get_domain(self, domain):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        if domain is None:
            return "Please supply a domain. Ex. example.com"
        else:
            domain_url = self._domains + domain
            domain_info = get(domain_url, header=token)
            return domain_info

    def domain_records(self, domain):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        records_url = self._domains + domain + '/records'
        records = get(records_url, header=token)
        return records

    def get_domain_record(self, domain, domain_id):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        if domain_id is None:
            return "Please supply a domain record id."
        else:
            records_url = self._domains + domain + '/records/{ID}'.format(ID=domain_id)
            record = get(records_url, header=token)
            return record

    def droplets(self):
        token = {'Authorization': 'Bearer ' + self.token + ''}
        droplet_list = get(self._droplets, header=token)
        return droplet_list