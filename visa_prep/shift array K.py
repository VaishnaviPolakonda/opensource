n=int(input())
a=list(map(int,input().split()))
k=int(input())
k%=n
res=a[-k:]+a[:-k]
print(*res)
