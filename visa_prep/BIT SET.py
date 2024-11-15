a=int(input())
b=int(input())
if(a&(1<<(b-1)))!=0:
    print("true")
else:
    print("false")
