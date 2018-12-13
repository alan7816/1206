#使用ifconfg找出IP Address
ifconfig = 'eno33554944: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\n inet 202.100.1.138 netmask 255.255.255.0 broadcast 202.100.1.255\n inet6 fe80::20c:29ff:fe8d:5cb6 prefixlen 64 scopeid 0x20\n ether 00:0c:29:8d:5c:b6 txqueuelen 1000 (Ethernet)\n RX packets 0 bytes 0 (0.0 B)\n RX errors 0 dropped 0 overruns 0 frame 0\n TX packets 33 bytes 4290 (4.1 KiB)\n TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0\n\n'

import re
#先將資料以換行分割產生列表
ifconfig_list = ifconfig.split('\n')
#print(ifconfig_list)
#用疊代處理 將資料一行一行顯示
for x in ifconfig_list:
    #print(x)
    #先將x用空白分割產生列表,再將X列表的結果疊代處理
    for y in x.split():
     #print(z)
     #將符合IP格式的資料擷取出來
     if re.match('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',y):
        print(y)
    ##將符合MAC格式的資料擷取出來
     if re.match('(\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2})', y):
        print(y)

