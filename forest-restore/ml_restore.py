from multiprocessing import Pool, Value
from requests.auth import HTTPDigestAuth
import optparse
import requests
import ConfigParser
import logging

# logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

# Command line argument parsing
parser = optparse.OptionParser()
parser.add_option("--config-file", dest="configfile", action="store", help="Specify the config file")
parser.add_option("--user", dest="username", action="store", help="Specify the username")
parser.add_option("--password", dest="password", action="store", help="Spec")
parser.add_option("--max-threads",dest="maxthreads", action="store", help="Specify maximum parallel forest restore")
options, args = parser.parse_args()

link = "http://localhost:8000/v1/eval"
failed = []
backup_configs=[]
f = open(options.configfile)

logging.info("Reading configuration file")
for line in f:
    backup_configs.append(line)

def run_restore(backup_config):
    forest_name = backup_config.split(':')[0]
    backup_path = backup_config.split(':')[1]
    logging.info(forest_name + " restore started from " + backup_path)
    script = """xquery=
    xquery version "1.0-ml";
    import module namespace admin = "http://marklogic.com/xdmp/admin"
    		  at "/MarkLogic/admin.xqy";
    xdmp:forest-restore(admin:forest-get-id(admin:get-configuration(), \"""" + forest_name +"""\"), \"""" + backup_path.rstrip() + """\")"""
    r=requests.post(link, data=script, auth=HTTPDigestAuth(options.username, options.password))
    if r.status_code == 200:
        logging.info(forest_name + " forest restore COMPLETED")
    else:
        logging.error(forest_name + " forest restore FAILED")

pool = Pool(processes=int(options.maxthreads))
pool.map(run_restore, backup_configs)
pool.close()  # worker processes will terminate when all work already assigned has completed.
pool.join()  # to wait for the worker processes to terminate.

logging.info("DONE")
