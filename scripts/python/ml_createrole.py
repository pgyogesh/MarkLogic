#!/usr/bin/env python
from string import Template
from requests.auth import HTTPDigestAuth
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-r','--rolename',
                    required=True,
                    help='The name of the role to be created.'
                    )
parser.add_argument('-d','--description',
                    default='No description',
                    help='A description of the role to be created.',
                    )
parser.add_argument('-m','--memberof',
                    default='',
                    help='A sequence of role names to which the role is assigned.')
parser.add_argument('-p','--permissions',
                    default='',
                    help='The default permissions for the role.')
parser.add_argument('-c','--collection',
                    default='',
                    help="The default collections for the role.")

parser.add_argument('--host',
                    default='localhost',
                    help="Hostname or Host IP address for MarkLogic Server")

args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()


data= Template("""xquery=
    xquery version "1.0-ml";
    import module namespace sec="http://marklogic.com/xdmp/security" at
    "/MarkLogic/security.xqy";

    sec:create-role(
    $rolname,
    $description,
    ($rolnames),
    ($permissions),
    ($collection)
    )""")


script_data=data.substitute(
                            rolname=args.rolename,
                            description=args.description,
                            rolnames=args.memberof,
                            permissions=args.permissions,
                            collection=args.collection
                            )

headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': 'multipart/mixed; boundary=BOUNDARY',
    }

raw_link = Template("http://$host:8000/v1/eval?database=Security")
hostname = args.host
link = raw_link.substitute(host=hostname)

r=requests.post(link,headers=headers, data=script_data, auth=HTTPDigestAuth('admin', 'admin'))
print(r.status_code)
print(r.text)
