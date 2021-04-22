a = input("輸入N及M為:" ).split()
c = list()
i = 1
while i<=int(a[0]):
    b = input("輸入矩陣數值第"+str(i)+"列為:").split()
    c.append(b)
    i+=1
print(c)
for j in range(int(a[1])):
    s = ""
    for k in range(int(a[0])):
        s+=c[k][j] + " "
    print("輸出矩陣數值第"+str(j+1)+"列為:" +s)