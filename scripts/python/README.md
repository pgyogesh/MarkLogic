# Python Scripts
## 1. runXQuery.py
 * This script is to run XQuery scripts against MarkLogic Database Server.
 * This script is useful if your xquery result is in HTML format(example: ../XQuery/getUserDetails.xquery)
 * This script redirect result in file or it opens result in browser, depends on options you provide while running

 #### Help
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
 ## 2. ml_stop.py
  * This script is to stop or restart MarkLogic Server on localhost
  * If you want to restart MarkLogic Server on all configured hosts then you need to modify the script wherever xdml:shutdown() and xdmp:restart() is used like below:
      ```
          xdmp:shutdown(($hostid1,hostid2),"Stopping MarkLogic Server")
          xdmp:restart(($hostid1,hostid2),"Restarting MarkLogic Server")
      ```

  #### Help
  ```
  $ python ml_stop.py -h
  usage: ml_stop.py [-h] [-r] [-a]

  optional arguments:
  -h, --help     show this help message and exit
  -r, --restart  Restart MarkLogic Server
  -a, --quite    Non-Interactive Mode

  ```
