a = [0,0,0,1,1,2,2,0,0]
length = len(a)
res = []
c0 = 0
c1 = 0
c2 = 0
for i in a:
    if i ==0:
        c0+=1
    elif i == 1:
        c1+=1
    elif i ==2:
        c2+=1

for i in range (0,c0):
    res.append(0)
for i in range (0,c1):
    res.append(1)
for i in range (0,c2):
    res.append(2)

print(res)
