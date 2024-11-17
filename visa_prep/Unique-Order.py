def ue(a):
    seen=set()
    r=[]
    for n in a:
        if n not in seen:
            r.append(n)
            seen.add(n)
    return r
n=int(input())
a=list(map(int,input().split()))
print(*ue(a))
