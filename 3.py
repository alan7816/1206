#show ip interface 擷取

test = 'Vlan88                 192.168.50.1    YES NVRAM  up                    up  '
test1 ='GigabitEthernet1/0/1   unassigned      YES unset  up                    up '

# "+"代表至少出現過一次
# \w 字母大小寫
# \s 空白
# \d 數字   \d{1,3}代表數字出現過1-3次
# 出現( ) 內代表需要擷取的資料 沒(  )內的代表需要過濾掉
# .* 代表甚麼都符合
import re
report = re.match('(\w+\d+)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\w+\s+\w+\s+(\w+)\s+(\w+).*' ,test).groups()
report2 = re.match('(.*)\s+\w+\s+\w+\s+\w+\s+(\w+)\s+(\w+).*' ,test1).groups()
print(report)
print(report[0])
print(report[1])
print(report[2])
print(report[3])
print(report2)
print(report2[0])
print(report2[1])
print(report2[2])
