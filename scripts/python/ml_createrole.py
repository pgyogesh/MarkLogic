#!/usr/bin/env python
from string import Template
from requests.auth import HTTPDigestAuth
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-r','--rolename',
                    #dest='ROLENAME',
                    #action='store',
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

args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()


data= Template("""
    xquery=
    xquery version "1.0-ml";
    import module namespace sec="http://marklogic.com/xdmp/security" at
    "/MarkLogic/security.xqy";

    sec:create-role(
    $rolname,
    $description,
    ($rolnames),
    ($permissions),
    ($collection),
    )""")


xquery_script=data.substitute(
                            rolname=args.rolename,
                            description=args.description,
                            rolnames=args.memberof,
                            permissions=args.permissions,
                            collections=args.collection
                            )
print(xquery_script)

# sec:create-role(
#     "Temporary",
#     "Temporary worker access",
#     ("filesystem-access"),
#     (),
#     ("testDocument"))
#
#
#
# from string import Template
# s = Template('$who likes $what')
# s.substitute(who='tim', what='kung pao')
#
# data.substitute(rolname='yogesh',description='jadhav',rolnames='yj',permissions='perm',collection='col')
# 'tim likes kung pao'
