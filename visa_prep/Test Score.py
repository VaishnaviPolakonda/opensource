a,b,c=map(int,input().split())
if c%b==0 and c//b<=a:
    print("YES")
else:
    print("NO")
