# alexa-on-otc
PoC for how to hook up Amazon Alexa with Open Telekom Cloud

.h1 Raise your voice - How to connect Amazon Alexa to OpenStack

.h2 Prequisites

You should be familiar with python and OpenStack and of course should have an account on a OpenStack based Cloud.
Currently this Proof-of-Concept is fully hard-wired and does not allow any dynamic configuration of credentials! Your private credentials need to go to the cllouds.yml file and are used to connect in the backend to the cloud.

**Attention** Do not make this skill public, otherwise someone might have control over your tenant/project! **Attention**
### Components

There are only three components: 

- clouds.yml --> This is the config file for your credentials
- otc_api.py --> The backend functions to interact with the cloud
- __init__.py --> main programm for starting the app and interacting with Amazon ASK

### Usage

- Configure your credentials in clouds.yml The file needs to be placed in ~/.config/openstack/clouds.yml or the same directoy as the app. Test the connection to the cloud with the included test.py - it will connect to the cloud and list your virtual machines.
- Update otc-api.py to use the right creditials block from clouds.yml ( see `cloud = shade.openstack_cloud(cloud='otc-xxx')`)
- Run the main app with `python __main__.py` - this will start the app and listen on port localhost:5000 for connections.
- In a second shell run [ngrok](https://ngrok.com/) to tunnel the port 5000 to the outside world
- Configutre the URL from ngrok in your skill and rebuild the model. 

### Help / Contact

The video of the lighting talk at the OpenStack Summit in Berlin is available at https://openstack.org. There you will also find some PPT slides explaining the deatils behind.

For further questions feel free to contact me at sebastian.wenner@t-systems.com 



