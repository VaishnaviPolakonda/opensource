n=int(input())
a=list(map(int,input().split()))
m=0
c=0
for d in a:
    if d==0:
        c+=1
        m=max(m,c)
    else:
        c=0
print(m)
