import re
import json
from collections import defaultdict
from difflib import SequenceMatcher
from itertools import combinations


xml_file = open('xml-sample-file.xml', 'r').read()

notifications_count = len(re.findall('sendmenotifications>true', xml_file))
rich_users = {}

email_user = defaultdict(list)
names = []

for item in xml_file.split('</row>'):
    #task1
    if '<creditBalance>' not in item or '<name>' not in item:
        continue
    credit_balance = int(re.search(r'<creditBalance>(\d+)</creditBalance>', item).group(1))
    name = re.search(r'<name>(.*)</name>', item).group(1)
    if credit_balance > 50:
        rich_users[name] = credit_balance

    #task2
    email = re.search(r'<email>(.*)</email>', item).group(1)
    email_user[email].append(name)
    names.append(name)

output = {}
for email, username in email_user.items():
    if not len(username) > 1:
        continue 
    for user in username:
        output[user] = email

name_combinations = combinations(names, 2)
duplicate_names = []
for first_name, second_name in name_combinations:
    sqm = SequenceMatcher(None, first_name, second_name)
    if sqm.ratio() > 0.85:
        duplicate_names += [[first_name, second_name]]


print('notifications_count:', notifications_count)
print('rich_users:', rich_users)
json.dump(output, open('email_dupes.json', 'a'))
json.dump(duplicate_names, open('name_dupes.json', 'a'))
print('wrote json output')
