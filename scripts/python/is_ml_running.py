from string import Template
import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--host',
                    action='store',
                    required=True,
                    help='Hostname or IP Address')

args = parser.parse_args()
host = args.host
data = Template("http://$hostname:7997")

link = data.substitute(hostname=host)
try:
    ping_ml=requests.get(link)
    if ping_ml.status_code == 200:
        print("MarkLogic Server is running")
except  Exception:
    print("MarkLogic Server in not running")
