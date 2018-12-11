#Copy資料及排序練習
L1 = [4,5,7,1,3,9,0]
#L2複製L1資料
L2 = L1.copy()
#L2進行從小到大排序
L2.sort()

for i in range(len(L1)):
    print(L1[i],L2[i])

