import requests
import json
from datetime import datetime

base_url = 'https://api.digitalocean.com/v2'
header_type = "'Content-Type': 'application/json'"


def get(url, header, payload=None):
    if payload = None:
        data = requests.get(url, headers = header)
    else:
        data = requests.get(url, headers = header, params = payload)
    if data.status_code == 200:
        data = data.json()
    else:
        data = 'Unable to validate get request'

    return data

def post(url, header, payload=None):
    if payload = None:
        data = requests.get(url, headers = header)
    else:
        data = requests.get(url, headers = header, params = payload)
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
        self._droplets = '{BASE}/droplets/'.format(BASE=base_url)

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

    def get_droplet(self, droplet):
        if droplet is None:
            return "Please enter a droplet ID"
        else:
            token = {'Authorization': 'Bearer ' + self.token + ''}
            url = self._droplets + droplet
            droplet_info = get(url, header=token)
            return droplet_info

class Droplet(object):

    def __init__(self, token):
        self.token = token
        self._droplets = '{BASE}/droplets/'.format(BASE=base_url)

    def action(self, action=None, droplet_id=None):
        if action is None:
            return "Please enter an action: shutdown, reboot, etc"
        elif droplet_id is None:
            return "Please enter a droplet id"
        elif action == 'reboot' or 'restart':
            payload = {'type': 'reboot'}
        elif action == 'power cycle':
            payload = {'type': 'power_cycle'}
        elif action == 'shutdown':
            payload = {'type': 'shutdown'}
        elif action == 'power off':
            payload = {'type': 'power_off'}
        elif action == 'power on':
            payload = {'type': 'power_on'}

        url = self._droplets + droplet_id + '/actions'
        token = {'Authorization': 'Bearer ' + self.token + ''}
        droplet_action = post(url, header=token, payload=payload)
        return droplet_action

    def snapshot(self, name=None, droplet_id=None):
        if droplet_id is None:
            return 'Please enter a droplet id'

        if name is None:
            now = datetime.now()
            snapshot_name = "%s-%s-%s" % (now.year, now.strftime("%m"), now.strftime("%d"))
            payload = {'type': 'snapshot', 'name': snapshot_name}
        else:
            snapshot_name = name
            payload = {'type': 'snapshot', 'name': snapshot_name}

        url = self._droplets + droplet_id + '/actions'
        token = {'Authorization': 'Bearer ' + self.token + ''}
        snapshot_action = post(url, header=token, payload=payload)
        return snapshot_action

    def rename(self, droplet_id=None, name=None):
        if name is None:
            return 'Please enter a name'
        elif droplet_id is None:
            return 'Please enter a droplet ID'

        url = self._droplets + droplet_id + '/actions'
        payload = {'type': 'rename', 'name': name}
        droplet_rename = post(url, header=token, payload=payload)
        return droplet_rename


    def upgrade(self, droplet_id=None):
        if droplet_id is None:
            return 'Please enter a droplet ID'

        url = self._droplets + droplet_id + '/actions'
        payload = {'type': 'upgrade'}
        droplet_upgrade = post(url, header=token, payload=payload)
        return droplet_upgrade