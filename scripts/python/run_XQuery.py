#!/usr/bin/env python
import requests
import webbrowser
import argparse
import os
import sys
from string import Template
from requests.auth import HTTPDigestAuth
import time

parser = argparse.ArgumentParser()

parser.add_argument(
            '-d',
            '--database',
            action='store',
            required=True,
            help='Specify database to run script against')
parser.add_argument(
            '--host',
            default='localhost',
            action='store',
            help='Hostname or IP Address')
parser.add_argument(
            "-s", "--script",
            dest="script_filename",
            action='store',
            help="XQuery script to run",
            required=True)
parser.add_argument("-o", "--online",
            action="store_true",
            default=False,
            help="View result in browser")
parser.add_argument("-l", "--filename",
            dest="output_filename",
            action='store',
            help="Store result in file as HTML format")
args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()

#print("Running runXQuery.py with options" + str(args))

if not args.online and not args.output_file:
    parser.print_help()

# Link to requests.post
host = args.host
db = args.database
data = Template("http://$hostname:8000/v1/eval?database=$dbname")
link = data.substitute(hostname=host,dbname=db)



if args.online:
    script = args.script_filename
    path = os.path.abspath(script)
    with open(path) as script_data:
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'multipart/mixed; boundary=BOUNDARY',
            }
            #script_file = open(filename)
        r=requests.post(link, headers=headers, data=script_data, auth=HTTPDigestAuth('admin', 'admin'))
        html = r.text
        html_path = '/tmp/temp.html'
        url='file://' + html_path
        with open(html_path,'w') as f:
            f.write(html)
        webbrowser.open(url)

if args.output_filename:
    script = args.script_filename
    path = os.path.abspath(script)
    with open(path) as script_data:
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'multipart/mixed; boundary=BOUNDARY',
            }
            #script_file = open(filename)
        r=requests.post(link, headers=headers, data=script_data, auth=HTTPDigestAuth('admin', 'admin'))
        html = r.text
    output_file = args.output_filename
    output_path = os.path.abspath(output_file)
    with open(output_path,"w") as o_file:
        o_file.write(html)
