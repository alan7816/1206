#show mac address

mac =  '7    78e3.b5ba.bcb2    DYNAMIC     Gi2/0/5'

import re
report = re.match('(\d+)\s+(\w{1,4}.\w{1,4}.\w{1,4})\s+(\w+)\s+(.*)' ,mac).groups()

id = 'VLAN ID ：%s' %(report[0])
mac = 'MAC ADD：%s' %(report[1])
Type = 'Type：%s' %(report[2])
Interface = 'Interface：%s' %(report[3])
print(id)
print(mac)
print(Type)
print(Interface)