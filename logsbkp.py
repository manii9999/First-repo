import os
from datetime import date


os.popen("sudo su -")

now=date.today()



print("Back-up the logs under the root Directory")
directory="Logs_bkp_{}".format(now)
os.popen("sudo mkdir /root/%s"%(directory))
os.popen("sudo cp /var/log/auth* /root/%s"%(directory))
print("Failed logs backup")

print("No Changes")

