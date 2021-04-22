a = list()
b = ["國文","英文","微積分","體育","程式設計"]

i = 0 
for i in  range(len(b)):
    c = int(input(b[i]+":"))
    a.append(c)

d = sum(a)/len(b)
print("平均分數:",round(d,2))

j = 0
for j in range(len(a)):
    if a[j] == max(a):
        print("最高分科目:"+b[j]+str(a[j])+"分")
k = 0
for k in range(len(a)):
    if a[k] == min(a):
        print("最低分科目:"+b[k]+str(a[k])+"分")


