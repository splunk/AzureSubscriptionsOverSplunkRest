import requests
from requests.auth import HTTPBasicAuth 
def postSubscriptions(splunk_web_user, splunk_web_pass):
    
    url = "https://10.202.12.146:8089/servicesNS/nobody/Splunk_TA_microsoft-cloudservices/splunk_ta_mscs_mscs_azure_audit?output_mode=json&count=-1"
    basicauth = HTTPBasicAuth(splunk_web_user, splunk_web_pass)
    

    response = requests.get(url, auth=basicauth, verify=False).json()
    for name in response['entry']:
        print(name, '\n')

    return ('Success')

print(postSubscriptions('admin',
                        'Splunk.5'
                        ))
