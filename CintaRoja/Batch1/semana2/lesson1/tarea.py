l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        print i
        print (i%5)
        l.append(str(i))

print ','.join(l)