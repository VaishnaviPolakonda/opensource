v,c=input().split()
if (v=='R' and c=='S') or (v=='S' and c=='P') or (v=='P' and c=='R') :
    print("Vignesh")
elif(v=='R' and c=='S') or (c=='P' and v=='R') or (c=='S' and v=='P'):
    print("Charan")
else:
    print("NULL")
