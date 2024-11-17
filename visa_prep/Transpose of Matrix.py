n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
t=[[m[j][i] for j in range(n)] for i in range(n)]
for r in t:
    print(*r)
