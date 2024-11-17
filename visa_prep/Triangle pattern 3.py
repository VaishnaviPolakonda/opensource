n=int(input())
for i in range(1,n+1):
    lp=''.join(str(m) for m in range(1,i+1))
    rp=''.join(str(m) for m in range(i,0,-1))
    gap=' '*(2*(n-i))
    if i==n:
        print(lp+rp)
    else:
        print(lp+gap+rp)
