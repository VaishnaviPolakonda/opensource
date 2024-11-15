a=int(input())
for _ in range(a):
    x,n=map(int,input().split())
    p=x//10
    res=p*n
    print(res)
