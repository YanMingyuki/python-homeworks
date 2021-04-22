a = input("輸入一組四位數字為:").split()
for i in range(len(a)):
    a[i] = (int(a[i])+7)%10

b = a[0]
a[0] = a[2]
a[2] = b

c = a[1]
a[1] = a[3]
a[3] = c

f=""
for j in range(len(a)):
    f = str(f) + str(a[j])
print(f)