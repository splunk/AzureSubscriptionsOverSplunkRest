import requests

url = "https://localhost:8089/services/data/inputs/all?search=TA-MS-AAD&output_mode=json"

payload={}
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Authorization': 'Basic YWRtaW46U3BsdW5rLjU=',
  'Cookie': 'splunkd_8000=QIWr8JZo47hkfEw1TmMVHv_zoUGZWVdg0I7lTgTXz8NMObgA4WiLQkBA7wTyDmZpClCq26wdztfdYTr9^dO11tipGo2G_clOdEIpxpVk01QP7zIGFsXYXuy_xLCzXrzKZ7wq; splunkweb_csrf_token_8000=15658481517227332700'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
