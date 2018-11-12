import requests
import configparser
import shade
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable SSL warnings

# Initialize and turn on debug logging
shade.simple_logging(debug=True)
#shade.simple_logging(debug=False)

# Initialize cloud
# Cloud configs are read with os-client-config
cloud = shade.openstack_cloud(cloud='otc-xxx')

def vm_count():
	counttotal = []
	countactive = []
	countstopped = []
	for i in cloud.list_servers(bare=True):
		counttotal.append(i.name)
		if i.status == 'ACTIVE':
			countactive.append(i.name)
		elif i.status == 'SHUTOFF':
			countstopped.append(i.name)
	t = len(counttotal)
	a = len(countactive)
	s = len(countstopped)
	print "Total: " + str(t)
	print "Active: " + str(a)
	print "Stopped: " + str(s)
	return (t,a,s)
