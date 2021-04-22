c = input("輸入月租費型式及通話時間為:").split(",")
m = float(c[0])
n = float(c[1]) 
if m==186:
    a = n*0.09
    if a>186:
        if a > 186*2:
            f = a*0.8
        else:
            f = a*0.9
    else:
        f = m
elif m==386:
    a = n*0.08
    if a>386:
        if a > 386*2:
            f = a*0.7
        else:
            f = a*0.8
    else:
        f = m
elif m==586:
    a = n*0.07
    if a>586:
        if a > 586*2:
            f = a*0.6
        else:
            f = a*0.7
    else:
        f = m
elif m==986:
    a = n*0.06
    if a>986:
        if a > 986*2:
            f = a*0.5
        else:
            f = a*0.6
    else:
        f = m

print("通話費為:",round(f))