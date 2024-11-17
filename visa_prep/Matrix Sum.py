n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
rs=[sum(m[i]) for i in range(n)]
cs=[sum(m[i][j] for i in range(n)) for j in range(n)]
r=[rs[i]+cs[i] for i in range(n)]
print(" ".join(map(str,r)))
