n=int(input())
s=input()
t=input()
def ai(s,t):
    mt={}
    ms={}
    for cs,ct in zip(s,t):
        if mt.get(cs,ct)!=ct or ms.get(ct,cs)!=cs:
            return False
        mt[cs]=ct
        ms[ct]=cs
    return True
print("true" if ai(s,t) else "false")
