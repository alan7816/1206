#格式對齊
department1 = 'security'
department2 = 'python'
depart1_m = 'cq'
depart2_m = 'qinke'
course1 = 123678.34324
course2 = 987654

#-10s左對齊空格10行
#10s 右對齊空格10行
#-10.2f 左對齊空格10行 取小數第二位
#s=文字 f=浮點數 d=整數
line1 = 'department1 name: %-10s manager:%-10s fees:%-10.2f the end!' %(department1,depart1_m,course1)
line2 = 'department2 name: %-10s manager:%-10s fees:%-10d the end!' %(department2,depart2_m,course2)
print(line1)
print(line2)