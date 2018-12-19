import os

#建立test資料夾
os.mkdir('test')
#進入test資料夾
os.chdir('test')
#建立一個qytang1文件
qytang1 = open('qytang1', 'w')
#qytang1文件寫入test.file
qytang1.write('test file\n')
#qytang1文件寫入this is tytang
qytang1.write('this is qytang\n')
#關閉qytang1文件
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
#建立qytang4資料夾
os.mkdir('qytang4')
os.mkdir('qytang5')

qytang_file_list = []
#顯示所有檔案
file_list = os.listdir()

for file in file_list:
    #檢查哪些檔案是文件
    if os.path.isfile(file):
        #讀取文件內容並一行一行顯示
        for file_line in open(file):
            if 'qytang' in file_line:
                qytang_file_list.append(file)

print('文件中包含"qytang"关键字的文件为:')
for file in qytang_file_list:
    print('\t', end='')
    print(file)
print('\n')