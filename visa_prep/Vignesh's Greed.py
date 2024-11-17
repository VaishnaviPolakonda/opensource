n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True)
for i in range(n-2):
    if s[i]<s[i+1]+s[i+2]:
        print(s[i]+s[i+1]+s[i+2])
        break
else:
    print(-1)
