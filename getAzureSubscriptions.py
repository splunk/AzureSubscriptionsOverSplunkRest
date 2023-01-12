import requests
from requests.auth import HTTPBasicAuth 

def getSubscription (splunk_web_user, splunk_web_pass):
    url = "https://localhost:8089/services/data/inputs/all?search=TA-MS-AAD&output_mode=json"
    basicauth = HTTPBasicAuth(splunk_web_user, splunk_web_pass)
    
    response = requests.get(url, auth=basicauth, verify=False).json()
    #print(response['entry'])
    for sub in response['entry']:
        print(sub)
        print('\n')

    return ('Success')


print(getSubscription('admin', 'Splunk.5'))
