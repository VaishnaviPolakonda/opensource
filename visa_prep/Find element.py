def b(a,x):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            return m
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
    return -1
n=int(input())
a=list(map(int,input().split()))
x=int(input())
r=b(a,x)
print(r)
