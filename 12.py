a = input("輸入一整數序列為:").split()
b = list()
for i in range(len(a)):
    sum1 = a.count(a[i])
    b.append(sum1)
    sum1 = 0
c = max(b)

if c >= len(a)/2:
    for j in a :
        if a.count(j) == c:
            print("過半元素為:",j)
            break
else:
    print("過半元素:NO")