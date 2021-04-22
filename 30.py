a = int(input("小明身上有幾元:"))
b = int(input("販賣機有幾種飲料:"))
i=1
c = list()
while i <= b:
    d = int(input(""))
    c.append(d)
    i += 1
j=0
sum1 =0
for j in range(len(c)):
    if a >= c[j] :
        sum1 += 1
    else:
        sum1=sum1
print(sum1)