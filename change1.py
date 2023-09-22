import os
from json import dumps
from httplib2 import Http

def notify(load):

    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAAo8zqJIs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=1PJWMfIRxN67yEXanosDpGEQItSCPuPRF6_usxvFBfE%3D'
    bot_message = {
            'text' : "===========POD2-2ADC3-MASTERDB==========\n" + "Load Average:  " +  final_load}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )


cmd = os.popen("uptime |awk '{print $9}' | head -1").read().strip()

print(cmd)

cmd = str(cmd.replace(',' , ''))

cmd = float(cmd)


#load1, load5, load15 = os.getloadavg()
#print (load1)
#cmd = float(load1)

#print(load1)


load = os.popen("uptime |awk '{print $9,$10,$11}' | head -1").read().strip()

final_load = str(load)

#with open("/proc/loadavg", "r") as file:

 #   load = str(file.read().strip())

  #  l = len(load)

   # final_load = load[:l-13]


if cmd  >= 0.00:

    notify(load)