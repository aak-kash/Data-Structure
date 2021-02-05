#revrse string/list 
a = [1,2,3,5,7]
aRev = []
lenA = len(a)
for i in range (0,len(a)):
    aRev.append(a[lenA-1])
    lenA= lenA-1
print(aRev)
