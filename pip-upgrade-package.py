from subprocess import call
import os
import json

cc = os.popen('pip list --outdate --format=json')
cc = cc.read()
print(cc)
cc = json.loads(cc)
for dist in cc:
    print(dist['name'])
    call("pip3 install --upgrade " + dist['name'], shell=True)



from subprocess import call
import os
import json

cc = os.popen('pip list --outdate --format=json')
cc = cc.read()
print(cc)
cc = json.loads(cc)
for dist in cc:
    print(dist['name'])
    call("pip3 uninstall -y " + dist['name'], shell=True)
