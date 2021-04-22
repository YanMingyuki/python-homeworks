b = list(input("輸入答案為(4位數):"))
c = list(input("please your number: "))       #猜數字遊戲
A=0
B=0
k=0
while True :
    str1 = ""
    for k in range(4):
        str1 += c[k]
    if str1 == "0000":
        break
    else:
        for i in range(len(b)):
            for j in range(len(c)) :
                if j == i and b[i] == c[j]:
                    A+=1
                    break
                elif b[i] == c[j] :
                    B+=1
                    break
        print(A,"A",B,"B")
        A=0
        B=0
        c = list(input("please your number: ")) 
    