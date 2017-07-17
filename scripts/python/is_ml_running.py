import requests
try:
    ping_ml=requests.get('http://localhost:7997')
    if ping_ml.status_code == 200:
        print("MarkLogic Server is running")
except  Exception:
    print("MarkLogic Server in not running")
