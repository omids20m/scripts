#! /usr/bin/python3

# 2024-09-21-1225

import requests
import logging
# import json
# python -m pip install requests
# https://github.com/perico85/auto_dns_ip_renew_to_cloudflare/blob/main/auto_dns.py

logging.basicConfig(
         format='%(asctime)s %(levelname)-8s %(message)s',
         level=logging.INFO,
         datefmt='%Y-%m-%d %H:%M:%S')

#auth_email="omids20m@gmail.com"
api_token="abd123xyz"
auth_key="efg456jkl"


# Account id abcd123xyz
# Zone id hiomid.com efgh456ijk

CONFIG = {
    'api_token': api_token,
    'zone_id': 'ijijijijijijijijijij', # hiomid.com
    'records': [
      {
          'name': 'hiomid.com',
          'record_id': 'mno789pqr'
      }
    ]
}

public_ip = requests.get('https://ipv4.icanhazip.com').text.strip()

try:
    with open('last_ip.txt', 'r') as ip_file:
        last_ip = ip_file.read().strip()
except FileNotFoundError:
    last_ip = None

#if public_ip != last_ip:
for record in CONFIG['records']:
  url = f'https://api.cloudflare.com/client/v4/zones/{CONFIG["zone_id"]}/dns_records/{record["record_id"]}'

  headers = {
      'Authorization': f'Bearer {CONFIG["api_token"]}',
      'Content-Type': 'application/json'
  }

  data = {
      'type': 'A',
      'name': record['name'],
      'content': public_ip,
      'ttl':   120,
      'proxied': False #True
  }

  response = requests.put(url, headers=headers, json=data)

  if response.status_code ==   200:
    logging.info('DNS record for {0} successfully updated..'.format(record["name"]))
    #print(f'DNS record for {record["name"]} successfully updated..')
  else:
    logging.info(f'Error updating the DNS record for {0}: {1}'.format(record["name"], response.content))
    #logging.debug('some debug text')
    #print(f'Error updating the DNS record for {record["name"]}: {response.content}')

  with open('last_ip.txt', 'w') as ip_file:
      ip_file.write(public_ip)
# else:
#   print("The IP hasn't changed, no need to update the DNS records.")
