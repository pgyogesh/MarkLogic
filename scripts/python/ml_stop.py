#!/usr/bin/env python
from requests.auth import HTTPDigestAuth
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-r',
                    '--restart',
                    default=False,
                    action="store_true",
                    help="Restart MarkLogic Server")
parser.add_argument('-a',
                    '--quite',
                    default=False,
                    action="store_true",
                    help="Non-Interactive Mode")
options = parser.parse_args()

def ml_stop():
    print("Stopping MarkLogic Server")
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'multipart/mixed; boundary=BOUNDARY',
        }
    data="""xquery=
            xquery version "1.0-ml";
            xdmp:shutdown((), "Shutting Down MarkLogic Server")"""
    requests.post('http://localhost:8000/v1/eval?database=Security', headers=headers, data=data, auth=HTTPDigestAuth('admin', 'admin'))

def ml_restart():
    print("Restarting MarkLogic Server")
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'multipart/mixed; boundary=BOUNDARY',
        }
    data="""xquery=
            xquery version "1.0-ml";
            xdmp:restart((), "Shutting Down MarkLogic Server")"""
    requests.post('http://localhost:8000/v1/eval?database=Security', headers=headers, data=data, auth=HTTPDigestAuth('admin', 'admin'))

if __name__ == '__main__':
    if options.quite:
        if options.restart:
            ml_restart()
        else:
            ml_stop()
    else:
        if options.restart:
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
