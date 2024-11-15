def r(n):
    s=-1 if n<0 else 1
    n=abs(n)
    r=int(str(n)[::-1])
    r*=s
    if r<-2**31 or r>2**31-1:
        return 0
    return r
n=int(input())
print(r(n))
