from multiprocessing import Pool, Value
import logging
import requests
import optparse
import re

# Command line options
parser = optparse.OptionParser()
parser.add_option("--source-database", dest = "sourcedatabase", action = "store", help = "Specify the source database to insert the documents")
parser.add_option("--dest-database", dest = "destdatabase", action = "store", help = "Specify the destination database to insert the documents")
parser.add_option("--source-host", dest = "sourcehost", default = "localhost", action = "store", help = "Specify the hostname or host IP of source MarkLogic Cluster")
parser.add_option("--dest-host"), dest = "desthost", action = "store", help = "Specify the hostname or host IP of destination MarkLogic Cluster")
parser.add_option("--source-port", dest = "sourceport", action = "store", help = "Specify the port number of source http application server through which you want to insert documents")
parser.add_option("--dest-port", dest = "destport", action = "store", help = "Specify the port number of destination http application server through which you want to insert documents")
parser.add_option("--parallel", dest = "parallel", default = 1, action = "store", help= "Specify the number of parallel processes")
parser.add_option("--uri-includes", dest ="uriincludes", action = "store", help = "Specify the part of uri you want to include" )

# Get values from command line

options, args = parser.parse_args()

if options.sourcedatabase:
	vSourceDatabase = options.sourcedatabase
else:
	logging.error("source database not specified... Exiting...")
	sys.exit()

if options.destdatabase:
	vDestDatabase = options.destdatabase
else:
	logging.error("destination database not specified... Exiting...")
	sys.exit()

vSourceHost = options.sourcehost
	
if options.desthost:
	vDestHost = options.desthost
else:
	logging.error("Destination host not specified... Exiting...")

if options.sourceport:
	vSourcePort = options.sourceport
else:
	logging.error("Source port not specified... Exiting...")

if options.destport:
	vDestpPort = options.destport
else:
	logging.error("Destination port not specified... Exiting...")

vParallel = options.parallel

if options.uriincludes:
	vUriIncludes = options.uriincludes
else:
	vUriIncludes = '*'

def get_uri()
	
