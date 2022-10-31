import random
import requests
import json

accounts=requests.get("http://127.0.0.1:8000/data")

api = json.loads(str(accounts))

print(accounts)
# def code():
#         for ac in accounts:
#             r = random.Random(ac)  
#             random_int=r.randint(350000,359999)
            
#             print (str(random_int) + " " + str(ac))

# code()