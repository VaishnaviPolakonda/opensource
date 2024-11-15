a,b,c=map(int,input().split())
tot=a*b
max_time=c*24*60
if tot<=max_time:
    print("YES")
else:
    print("NO")
