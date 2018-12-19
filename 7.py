import re

str1 = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

str1_list = str1.split()
#print(str1_list)

for x in str1_list:
    #print(x)
     if re.match('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', x):
    #if re.match('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', x):
      print(x)
