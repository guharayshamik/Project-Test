import requests
import json

print("Qust 4: Create Python REST client program which queries http://api.open-notify.org/astros.json and list the user name in sorted order. Convert the REST JSON object to list<String> with JSON names in sorted order.")
print("Ans: ")
response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
 jsonResponse = response.json()
 print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 print(" List of Name extracted from json displayed in Sorted order ")
 print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 for key, value in jsonResponse.items():
   if key == "people":
      name_sorted_in_list = sorted(value, key=lambda k: k['name'])
      for i in name_sorted_in_list:
          list_of_names=(i['name'])
          print(list_of_names)
      print("\n")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("JSON Object captured inside a list displayed based on sorted names")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print(name_sorted_in_list)
else:
    print("ENDPOINT_NOT_REACHABLE")
    exit()