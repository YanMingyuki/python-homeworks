total=i=1
m=int(input("請輸入階乘直M: "))    
while (total<=m):
    total*=i
    i+=1
print("超過M為"+str(m)+"的最小階乘N值為:",i-1)