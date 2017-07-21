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
  * This script is to stop or restart MarkLogic Server
  * By default, This script restarts the MarkLogic Server installed on localhost unless `--host` option is provided

  #### Help
  ```
  $ python ml_stop.py -h
  usage: ml_stop.py [-h] [-r] [-a]

  optional arguments:
  -h, --help     show this help message and exit
  -r, --restart  Restart MarkLogic Server
  -a, --quite    Non-Interactive Mode

  ```

## 3. ml_createrole.py
  * This script is to create role in MarkLogic.
  * By default, This script tries to run on Marklogic installed on localhost unless `--host` option is specified
  * We have to use two quotes while running this script like below:

  ```
  python ml_createrole.py -r '"rolename"' -d '"Role Name - MarkLogic DBA"' -m '"admin"' -c '"testDocument"' --host 192.168.2.10
  ```

  #### Help

  ```
  $ python ml_createrole.py --help
usage: ml_createrole.py [-h] -r ROLENAME [-d DESCRIPTION] [-m MEMBEROF]
                        [-p PERMISSIONS] [-c COLLECTION] [--host HOST]

optional arguments:
  -h, --help            show this help message and exit
  -r ROLENAME, --rolename ROLENAME
                        The name of the role to be created.
  -d DESCRIPTION, --description DESCRIPTION
                        A description of the role to be created.
  -m MEMBEROF, --memberof MEMBEROF
                        A sequence of role names to which the role is
                        assigned.
  -p PERMISSIONS, --permissions PERMISSIONS
                        The default permissions for the role.
  -c COLLECTION, --collection COLLECTION
                        The default collections for the role.
  --host HOST           Hostname or Host IP address for MarkLogic Server

  ```

## 4. is_ml_running.py

  * This script is to check if MarkLogic Server is running
  * By default it checks on localhost unless `--host` option is provided

  #### Help

  ```
  $ python is_ml_running.py --help
usage: is_ml_running.py [-h] [--host HOST]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Hostname or IP Address
  ```
