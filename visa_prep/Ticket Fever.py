m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    st=max(0,a-b)
    print(st)
