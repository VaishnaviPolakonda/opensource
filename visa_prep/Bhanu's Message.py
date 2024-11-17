def iv(m):
    if len(m)<10 or len(m)>20:
        return False
    if m[0]=='+':
        m=m[1:]
    if not all(c.isdigit() or c==' ' for c in m):
        return False
    n=m.split()
    if len(n)==2:
        co,p=n[0],n[1]
        if not(len(co)==2 and co.isdigit()):
            return False
    elif len(n)==1:
        p=num[0]
    else:
        return False
    if len(p)!=10 or not p.isdigit():
        return False
    s=sum(int(digit) for digit in p)
    return s>0
if __name__=="__main__":
    m=input().strip()
    if iv(m):
        print("Correct")
    else:
        print("Incorrect")
