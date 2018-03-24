import json
import requests

# Download AWS Ip ranges
ip_range_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

def get_ranges(url_addr):
    response = requests.get(url_addr)
    # Parse JSON response
    ranges = response.json()
    return ranges

ip_range = get_ranges(ip_range_url)
my_range = (ip_range['prefixes'])


def splitfile(**kwargs):
    syncToken, createDate, prefixes, ipv6_prefixes = kwargs.values()
    print(syncToken, createDate)
    for prefix in prefixes:
        print(prefix['ip_prefix'])

rangit = ip_range['prefixes']

splitfile(**ip_range)
# data = get_ranges(ip_range_url)
# sync_token = data['syncToken']
# create_date = data['createDate']
# # print(data)
# prefixes= data['prefixes']
#
# for prefix in prefixes:
#   print(prefix.items())
# for prefix in prefixes:
#     # if prefix['region'] == 'us-west-2':
#     #     print(prefix['ipv6_prefix'], prefix['region'])
#     #
#     print(prefix['ip_prefix'])ip_prefix

# for prefix in prefixes:
#     for ip_prefix in prefix:
#         print(ip_prefix, region, service)

# for prefix in data['prefixes']:
#     print(prefix)


# print("Response object: ", response)
# #print("Response json: ", data)
# print("SyncToken: ", sync_token)
# print("Create Date", create_date)
# # print("Prefixes\n", data['prefixes'])
#

