a = int(input("輸入第一行正整數:"))
b = input("第二行中數列中的數字為:").split()
c = list()
i = 1
print(b)
sum1 = 0
while i<=a:
    j=0
    for j in range(len(b)):
        if int(b[j]) == i :
            sum1 = sum1 + 1
        else:
            sum1 = sum1
    c.append(sum1)
    sum1 =0
    i+=1

d = max(c)
if d == 1:
    print("每個數字剛只出現1次")
else:
    for n in b:
        if b.count(n)==d:
            print("最大出現的次數為:",n)
            print("出現次數為:",d)
            break