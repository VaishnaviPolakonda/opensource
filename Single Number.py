def f(a):
    r=0
    for n in a:
        r^=n
    return r
n=int(input())
a=list(map(int,input().split()))
print(f(a))
