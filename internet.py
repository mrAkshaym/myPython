import requests

#persons in space
response = requests.get("http://api.open-notify.org/astros.json")

#print(response.status_code)
#print(response.json())

json = response.json()
if (json['message'] == 'success'):
    list = json['people']
    for member in list:
        print(member['name'])
else:
    print("Error fetching data")