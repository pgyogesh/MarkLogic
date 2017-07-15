# Python Scripts
## runXQuery.py
 * This script is to run XQuery scripts against MarkLogic Database Server.
 * This script is useful if you xquery result is in HTML format(example: ../XQuery/getUserDetails.xquery)
 * This script redirect result in file or it opens result in browser, depends on options you provide while running
 
 ```
 $ python run_XQuery.py -h
usage: run_XQuery.py [-h] -s SCRIPT_FILENAME [-o] [-l OUTPUT_FILENAME]
optional arguments:
  -h, --help            show this help message and exit
  -s SCRIPT_FILENAME, --script SCRIPT_FILENAME
                        XQuery script to run
  -o, --online          View result in browser
  -l OUTPUT_FILENAME, --filename OUTPUT_FILENAME
                        Store result in file as HTML format

 ```   
    
