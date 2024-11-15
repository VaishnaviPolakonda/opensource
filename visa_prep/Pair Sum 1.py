n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=set()
f=False
for b in a:
    if k-b in s:
        f=True
        break
    s.add(b)
print("true" if f else "false")
