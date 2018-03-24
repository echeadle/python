import json
import requests

# Download AWS Ip ranges
ip_range_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

# Parse JSON response
def get_ranges(url_addr):
    response = requests.get(url_addr)
    ranges = response.json()
    return ranges

ip_range = get_ranges(ip_range_url)
my_range = (ip_range['prefixes'])


def split_ranges(**kwargs):
    syncToken, createDate, prefixes, ipv6_prefixes = kwargs.values()
    print(syncToken, createDate)
    for prefix in prefixes:
        print(prefix['ip_prefix'])


split_ranges(**ip_range)

