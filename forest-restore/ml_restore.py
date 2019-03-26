from multiprocessing import Pool
from requests.auth import HTTPDigestAuth
import optparse
import requests
import ConfigParser
import logging

# Command line argument parsing
parser = optparse.OptionParser()
parser.add_option("-c","--config-file", dest="configfile", action="store", help="Specify the config file")
parser.add_option("-u","--user", dest="username", action="store", help="Specify the username")
parser.add_option("-w","--password", dest="password", action="store", help="Spec")
parser.add_option("-p","--max-threads",dest="maxthreads", action="store", help="Specify maximum parallel forest restore")
parser.add_option("-v","--verbose", action="store_true", dest="verbose", help="Enable verbose logging")

options, args = parser.parse_args()

# logging
if options.verbose:
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

link = "http://localhost:8000/v1/eval"
backup_configs=[]

logging.info("Reading configuration file")
f = open(options.configfile)
for line in f:
    backup_configs.append(line)
f.close()

def run_restore(backup_config):
    forest_name = backup_config.split(':')[0]
    backup_path = backup_config.split(':')[1].rstrip()
    logging.info(forest_name + " restore started from " + backup_path)
    script = """xquery=
    xquery version "1.0-ml";
    import module namespace admin = "http://marklogic.com/xdmp/admin"
    		  at "/MarkLogic/admin.xqy";
    xdmp:forest-restore(admin:forest-get-id(admin:get-configuration(), \"""" + forest_name +"""\"), \"""" + backup_path + """\")"""
    r=requests.post(link, data=script, auth=HTTPDigestAuth(options.username, options.password))
    if r.status_code == 200:
        logging.info(forest_name + " forest restore COMPLETED")
    else:
        logging.error(forest_name + " forest restore FAILED")
        logging.error(r.text)
        logging.info("Restore will continue for other forests")

pool = Pool(processes=int(options.maxthreads))
pool.map(run_restore, backup_configs)
pool.close()  # worker processes will terminate when all work already assigned has completed.
pool.join()  # to wait for the worker processes to terminate.

logging.info("DONE")
