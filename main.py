import requests
import csv
from conf.constants import MAGENTO_URL, AUTH, COL, API_URL

data = csv.DictReader(open('files/test.csv', 'r'))
for row in data:
    print('entity_id: ' + row[COL])
    url = "{}/{}/{}".format(MAGENTO_URL, API_URL, row[COL])
    print(url)
    headers = {
        'Authorization': 'Bearer {}'.format(AUTH),
    }
    request = requests.request("DELETE", url=url, headers=headers)
    print(request.text)
