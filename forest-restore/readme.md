# Introduction

Python script to restore Marklogic forest in parallel. This script can be used when we restore different number of forests in a database or when there is mismatch in database forest name and backup forest names.

## Help

```
Yogeshs-MacBook-Air:~ yogeshjadhav$ python ml_restore.py --help
Usage: ml_restore_new.py [options]

Options:
  -h, --help            show this help message and exit
  --config-file=CONFIGFILE
                        Specify the config file
  --user=USERNAME       Specify the username
  --password=PASSWORD   Spec
  --max-threads=MAXTHREADS
                        Specify maximum parallel forest restore
```
