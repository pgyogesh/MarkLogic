#!/usr/bin/env python
import requests
import webbrowser
import argparse
import os
import sys
from requests.auth import HTTPDigestAuth
import time

parser = argparse.ArgumentParser()
parser.add_argument(
            "-s", "--script",
            dest="script_filename",
            action='store',
            help="XQuery script to run",
            required=True)
            #metavar="FILE")
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

options = vars(args)

print("Running runXQuery.py with options" + str(options))

if not options['online'] and not options['output_filename']:
    parser.print_help()

if options['online']:
    script = options['script_filename']
    path = os.path.abspath(script)
    with open(path) as script_data:
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'multipart/mixed; boundary=BOUNDARY',
            }
            #script_file = open(filename)
        r=requests.post('http://localhost:8000/v1/eval?database=Security', headers=headers, data=script_data, auth=HTTPDigestAuth('admin', 'admin'))
        html = r.text
        html_path = '/tmp/temp.html'
        url='file://' + html_path
        with open(html_path,'w') as f:
            f.write(html)
        webbrowser.open(url)

if options['output_filename']:
    script = options['script_filename']
    path = os.path.abspath(script)
    with open(path) as script_data:
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'multipart/mixed; boundary=BOUNDARY',
            }
            #script_file = open(filename)
        r=requests.post('http://localhost:8000/v1/eval?database=Security', headers=headers, data=script_data, auth=HTTPDigestAuth('admin', 'admin'))
        html = r.text
    output_file = options['output_filename']
    output_path = os.path.abspath(output_file)
    with open(output_path,"w") as o_file:
        o_file.write(html)





# def run_xquery(filename = xquery_script):
#     headers = {
#         'Content-type': 'application/x-www-form-urlencoded',
#         'Accept': 'multipart/mixed; boundary=BOUNDARY',
#     }
#
#     #script_file = open(filename)
#     r=requests.post('http://localhost:8000/v1/eval?database=Security', headers=headers, data=filename, auth=HTTPDigestAuth('admin', 'admin'))
#     html = r.text
#     return html
#
# def writeToFile(file):
#     #path= = os.path.abspath('UserDetails.html')
#     #url='file://' + path
#     #with open(path,'w') as f:
#         file.write(run_xquery())
#     #path = os.path.abspath('temp.html')
#     #url='file://' + path
#     #with open(path,'w') as f:
#     #   f.write(html)
#     #webbrowser.open(url)
#
# def openInBrowser():
#     path = os.path.abspath('temp.html')
#     url='file://' + path
#     with open(path,'w') as f:
#        f.write(html)
#     webbrowser.open(url)
#
# if __name__ == '__main__':
#
