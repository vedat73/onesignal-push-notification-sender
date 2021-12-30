import requests

data = { "app_id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", 
        "filters":[{ "field":"tag" ,"key":"user_name","relation":"=","value":"vedat123" } ],  
        "contents": {"en": "This is my notification contents"},
        "headings": {"en": "This is my notification title"},
        "data":{"whoami" : "nobody"} }
requests.post("https://onesignal.com/api/v1/notifications",headers={"Authorization": "Basic OneSignal-Rest-Api-Key"},    json=data)
print("gone")


