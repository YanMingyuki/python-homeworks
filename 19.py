a = int(input("組數為:"))
i=1
while i<=a:
    b = input("第"+str(i)+"組:").split()
    sum1 = int(b[0])*250+int(b[1])*175
    print("第",i,"組應收費用:",sum1)
    i+=1


