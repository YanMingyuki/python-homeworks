a = input().split()
c = list()
i = 1
while i<=int(a[0]):
    b = input().split()
    c.append(b)
    i+=1

x = input().split()
z = list()
j = 1
while j<=int(x[0]):
    y = input().split()
    z.append(y)
    j+=1

if a[0]==x[0] and a[1]==x[1]:
    for k in range(int(a[0])):
        s = ""
        for l in range(int(a[1])):
            p = int(c[k][l])+int(z[k][l])
            s+=str(p) + " "
        print(s)
else:
    print("兩個矩陣無法相加")
