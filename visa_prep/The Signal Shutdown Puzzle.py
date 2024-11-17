def f(n,m,g):
    res=[r[:] for r in g]
    rtto=set()
    ctto=set()
    for i in range(n):
        for j in range(m):
            if g[i][j]==0:
                rtto.add(i)
                ctto.add(j)
    for i in range(n):
        for j in range(m):
            if i in rtto or j in ctto:
                g[i][j]=0
    for r in g:
        print(" ".join(map(str,r)))
n,m=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]
f(n,m,g)
