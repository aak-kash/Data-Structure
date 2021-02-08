a = [1,-2,4,-5,8,-9,10,11,-12]

aP = []
for i in a:
    if i<0:
        aP.append(i)
for i in a:
    if i>0:
        aP.append(i)
print(aP)
