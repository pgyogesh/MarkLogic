# Introduction

Python script to restore Marklogic forest in parallel. This script can be used when we restore different number of forests in a database or when there is mismatch in database forest name and backup forest names.

## Help

```
Yogeshs-MacBook-Air:~ yogeshjadhav$ python ml_restore_new.py --help
Usage: ml_restore_new.py [options]

Options:
  -h, --help            show this help message and exit
  -c CONFIGFILE, --config-file=CONFIGFILE
                        Specify the config file
  -u USERNAME, --user=USERNAME
                        Specify the username
  -w PASSWORD, --password=PASSWORD
                        Spec
  -p MAXTHREADS, --max-threads=MAXTHREADS
                        Specify maximum parallel forest restore
  -v, --verbose         Enable verbose logging
```
