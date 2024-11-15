n=input()
rs=""
c=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        c+=1
    else:
        rs+=n[i-1]+str(c)
        c=1
rs+=n[-1]+str(c)
print(rs)
