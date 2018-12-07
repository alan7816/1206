import random #導入random模組

#1-255隨機產生變數
section1 = random.randint(1,255)
section2 = random.randint(1,255)
section3 = random.randint(1,255)
section4 = random.randint(1,255)

#將變數組合成字串
#str將數字轉換成文字處理
random_ip = str(section1) + ' . ' + str(section2) + ' . ' + str(section3) + ' . ' + str(section4)

#顯示結果
print(random_ip)