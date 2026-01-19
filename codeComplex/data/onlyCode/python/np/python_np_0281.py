def l(a):
    b=bin(a)[2:]
    b="0"*(e-len(b))+b
    d=len(b)
    for i in range(d-1,-1,-1):
        if b[i]=="1":
            c=d-1-i
            break
    if c==0:
        return -1
    return (a-2**(c-1))

def r(a):
    b=bin(a)[2:]
    b="0"*(e-len(b))+b
    d=len(b)
    for i in range(d-1,-1,-1):
        if b[i]=="1":
            c=d-1-i
            break
    if c==0:
        return -1
    return (a+2**(c-1))
          
def u(a):
    b=bin(a)[2:]
    b="0"*(e-len(b))+b
    d=len(b)
    for i in range(d-1,-1,-1):
        if b[i]=="1":
            c=d-1-i
            break
    if c==d-1:
        return -1
    else:
        if b[d-1-c-1]=="0":
            return a+(2**c)
        else:
            return a-(2**c)
    
n,q=list(map(int,input().split()))
e=len(bin(n)[2:])
for i in range(q):
    a=int(input())
    b=input()
    for i in range(len(b)):
        if b[i]=="U":
            c=u(a)
            if c!=-1:
                a=c
        elif b[i]=="R":
            c=r(a)
            if c!=-1:
                a=c
        elif b[i]=="L":
            c=l(a)
            if c!=-1:
                a=c
    print(a)