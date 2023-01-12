import requests
from requests.auth import HTTPBasicAuth 
def postSubscriptions(splunk_web_user, splunk_web_pass, subscriptionList):
    
    url = "https://localhost:8089/servicesNS/nobody/TA-MS-AAD/TA_MS_AAD_azure_subscription?output_mode=json"
    basicauth = HTTPBasicAuth(splunk_web_user, splunk_web_pass)
    

    if (len(subscriptionList) != 0):
        for sub in subscriptionList:
            payload='name='+str(sub)+'&interval=86400&index=default&azure_app_account=AzureAccount&tenant_id=123456&environment=public&source_type=azure%3Asubscriptions'
            response = requests.post(url, auth=basicauth, data=payload, verify=False).json()
            print(response)
    return "Success"

print(postSubscriptions('admin','Splunk.5',['Subscription8']))
