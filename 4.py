#show mac address

mac =  '7    78e3.b5ba.bcb2    DYNAMIC     Gi2/0/5'

import re
report = re.match('(\d+)\s+(\w{1,4}.\w{1,4}.\w{1,4})\s+(\w+)\s+(.*)' ,mac).groups()

id = '%-10s：%s' %('VLAN ID',report[0])
mac = '%-10s：%s' %('MAC ADD',report[1])
Type = '%-10s：%s' %('Type',report[2])
Interface = '%-10s：%s' %('Interface',report[3])
print(id)
print(mac)
print(Type)
print(Interface)