a = input("檢測的字串(end結束):")
b = input("檢測的單一字元:")
while a != "end":
    if b in a:
        s = a.count(b)
        print("字元"+str(b)+"出現次數為:",s)
    else:
        print("字元"+str(b)+"不存在")
    a = input("檢測的字串(end結束):")
    b = input("檢測的單一字元:")
