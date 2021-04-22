a=list(input("輸入值為:"))
z=a
for j in range(len(a)-2):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            b = a[i]
            a[i] = a[i+1]
            a[i+1] = b

d=""
for c in range(len(a)):
    d = str(d) + str(a[c])  

for x in range(len(z)-1):
    for y in range(len(z)-1):
        if z[y]<z[y+1]:
            b = z[y]
            z[y] = z[y+1]
            z[y+1] = b

f=""
for e in range(len(z)):
    f = str(f) + str(z[e]) 
    
print(int(f)-int(d))