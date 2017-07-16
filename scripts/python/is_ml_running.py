import requests
try:
    ping_ml=requests.get('http://localhost:7997')
    if ping_ml.status_code == 200:
        print("MarkLogic Server is running")
except Exception as e:
    print(e)
    print("MarkLogic Server in not running")
# if ping_ml.status_code == 200:
#     print("MarkLogic Server is running")
# else:
#     print("MarkLogic Server is not running")
