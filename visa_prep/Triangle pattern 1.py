n=int(input())
c=1
for i in range(1,n+1):
    m=[]
    for j in range(i):
        m.append(c)
        c+=1
    print(" ".join(map(str,m)))
