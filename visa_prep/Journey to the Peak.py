n=int(input())
a=list(map(int,input().split()))
ca=0
ma=0
for h in a:
    ca+=h
    ma=max(ma,ca)
print(ma)
