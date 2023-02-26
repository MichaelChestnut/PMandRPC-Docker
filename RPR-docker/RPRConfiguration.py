resetpin = 4 #IO pin 4 not actually pin 4 (actually pin 7 on Pi4). Change to any GPIO pin
topic = "RemotePiReset" #topic name
broker = "ccrisupe3.iot.nau.edu" #broker name or IP address
client = "ccriiobe3.iot.nau.edu" #client name or IP address
cacert = "/SOME/PATH/TO/YOUR_CAFILE.crt" #path to cafile
certfile = "/SOME/PATH/TO/YOUR_CERTFILE.crt" #path to certfile
keyfile = "/SOME/PATH/TO/YOUR_KEYFILE.key" #path to keyfile
timezone = 'US/Arizona' #timezone for timestamps, consult pytz list of timezones for acceptable timezones
