import requests

def postSubscriptions(subscriptionList):
    
    url = "https://localhost:8089/servicesNS/nobody/TA-MS-AAD/TA_MS_AAD_azure_subscription?output_mode=json"
    print(subscriptionList)
    if (len(subscriptionList) != 0):
        for sub in subscriptionList:
            payload='name='+str(sub)+'&interval=86400&index=default&azure_app_account=AzureAccount&tenant_id=123456&environment=public&source_type=azure%3Asubscriptions'
            headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': 'Basic YWRtaW46U3BsdW5rLjU=',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'splunkd_8000=QIWr8JZo47hkfEw1TmMVHv_zoUGZWVdg0I7lTgTXz8NMObgA4WiLQkBA7wTyDmZpClCq26wdztfdYTr9^dO11tipGo2G_clOdEIpxpVk01QP7zIGFsXYXuy_xLCzXrzKZ7wq; splunkweb_csrf_token_8000=15658481517227332700'
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            response = response.text 
            print(response)
    return "Success"

print(postSubscriptions(['Subscription6', 'Subscription7']))
