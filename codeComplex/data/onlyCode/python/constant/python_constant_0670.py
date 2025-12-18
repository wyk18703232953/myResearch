import sys
keta=29
print("?",0,0,flush=True)


A00=int(input())
if A00==0:
    ANS=0
    for k in range(keta,-1,-1):
        print("?",2**k,0,flush=True)
        if int(input())==-1:
            ANS+=2**k
    print("!",ANS,ANS,flush=True)
    sys.exit()


A=0
B=0
for k in range(keta,-1,-1):
    LIST=[]
    print("?",2**k+A,B,flush=True)
    LIST.append(int(input()))
    print("?",A,2**k+B,flush=True)
    LIST.append(int(input()))

    if LIST[0]!=LIST[1]:
        if LIST[0]==-1:
            A+=2**k
            B+=2**k

    else:
        if A00==1:
            A+=2**k
        else:
            B+=2**k
        A00=LIST[0]
print("!",A,B,flush=True)
        
        
