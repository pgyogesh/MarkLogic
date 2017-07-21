#!/usr/bin/env python
from string import Template
from requests.auth import HTTPDigestAuth
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-r',
                    '--restart',
                    default=False,
                    action="store",
                    help="Restart MarkLogic Server")
parser.add_argument('-a',
                    '--quite',
                    default=False,
                    action="store_true",
                    help="Non-Interactive Mode")

parser.add_argument('--host',
                    #default='localhost',
                    action='append',
                    required=True,
                    help='Hostname or IP Address')

args = parser.parse_args()

host = args.host


def ml_stop():
    print("Stopping MarkLogic Server")
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'multipart/mixed; boundary=BOUNDARY',
        }
    data="""xquery=
            xquery version "1.0-ml";
            xdmp:shutdown((), "Shutting Down MarkLogic Server")
        """
    requests.post(link, headers=headers, data=data, auth=HTTPDigestAuth('admin', 'admin'))

def ml_restart():
    print("Restarting MarkLogic Server")
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'multipart/mixed; boundary=BOUNDARY',
        }
    data="""xquery=
            xquery version "1.0-ml";
            xdmp:restart((), "Shutting Down MarkLogic Server")"""
    requests.post(link, headers=headers, data=data, auth=HTTPDigestAuth('admin', 'admin'))

if __name__ == '__main__':
    hosts = args.host
    for host in hosts:
        data = Template("http://$hostname:8000/v1/eval")
        link = data.substitute(hostname=host)
        try:
            ping_ml_data=Template('http://$localhost:7997')
            ping_ml_link=data.substitute(hostname=host)
            ping_ml=requests.get(ping_ml_link)
            if ping_ml.status_code == 200:
                print("MarkLogic Server is running in " + host)
        except  Exception:
            print("MarkLogic Server in not running " + host)

        if args.quite:
            if args.restart:
                ml_restart()
            else:
                ml_stop()
        else:
            if args.restart:
                a=input("This action will restart the MarkLogic Server. Are you sure?(Yy|Nn)")
                if a in ('Y','y'):
                    ml_restart()
                else:
                    print("User aborted, Exiting...")
                    sys.exit()
            else:
                a=input("This action will stop the MarkLogic Server. Are you sure?(Yy|Nn)")
                if a in ('Y','y'):
                    ml_stop()
                else:
                    print("User aborted, Exiting...")
                    sys.exit()
