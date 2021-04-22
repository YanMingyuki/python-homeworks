a = input().split()

sum1=0
for i in range(len(a)):
    if a[i] == "A":
        sum1+=14
    elif a[i] == "K":
        sum1+=13
    elif a[i] == "Q":
        sum1+=12
    elif a[i] == "J":
        sum1+=11
    else:
        sum1+=int(a[i])
print(sum1)