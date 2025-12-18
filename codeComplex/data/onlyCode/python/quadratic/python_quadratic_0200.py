s, l= list(map(int,input().split()))
sig = []
utp = []
if s == 0 or l ==0:
    print('NO')
    quit()
for i in range(s):
    sig.append(list(map(int,input())))
for i in range(0,l):
    out = 0
    for x in range(0,s):
        out+=sig[x][i]
    utp.append(out)
sig = sorted(sig,key = sum)
for i in range(0,s):
    res1=0
    for x in range(0,l):
        if utp[x]-sig[i][x] <=0:
            break
        else:
            res1+=1
    if res1 == l:
        print('YES')
        quit()
        
print('NO')
