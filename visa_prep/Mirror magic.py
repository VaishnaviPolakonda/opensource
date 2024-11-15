p=int(input())
m=[list(map(int,input().split()))for _ in range(p)]
for r in m:
    print(*r[::-1])
