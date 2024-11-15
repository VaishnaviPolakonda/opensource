def fact(a):
    if a==0:
        return 1
    res=1
    for i in range(1,a+1):
        res*=i
    return res
a=int(input())
print(fact(a))
