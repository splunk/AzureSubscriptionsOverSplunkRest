import requests
from requests.auth import HTTPBasicAuth 
def postSubscriptions(splunk_web_user, splunk_web_pass, account, subid, interval, index, inputlist):
    
    url = "https://10.202.12.146:8089/servicesNS/nobody/Splunk_TA_microsoft-cloudservices/splunk_ta_mscs_mscs_azure_audit?output_mode=json"
    basicauth = HTTPBasicAuth(splunk_web_user, splunk_web_pass)
    

    if (len(inputlist) != 0):
        for name in inputlist:
            payload='name='+str(name)+'&account='+account+'&subscription_id='+subid+'&interval='+interval+'&index='+index
            response = requests.post(url, auth=basicauth, data=payload, verify=False).json()
            print(response)
    return "Success"

print(postSubscriptions('admin',
                        'Splunk.5',
                        'sub-id',
                        '1234567',
                        '3600', 
                        'default',
                        ['azureaudit7', 'azureaudit8']
                        ))
