import shade
from munch import *
from pprint import *

# Initialize and turn on debug logging
#shade.simple_logging(debug=False)
shade.simple_logging(debug=True)

# Initialize cloud
# Cloud configs are read with os-client-config
cloud = shade.openstack_cloud(cloud='otc-201')

instances = cloud.list_servers(detailed=False,bare=True)
for instance in instances:
    pprint(unmunchify(instance))
    print "#########################"
