from copy import *
n,T=map(int,raw_input().split())
cl=set(())
di={(0,0,0,T):1}
for k in range(n):
    t,g=map(int,raw_input().split())
    an=deepcopy(di)
    for k in an:
        nc=list(k)
        nc[3]-=t
        nc[g-1]+=1
        if nc[3]>=0:
            nc=tuple(nc)
            if nc in di:
                di[nc] += an[k]
            else:
                di[nc] = an[k]
nd={(1,0,0,0):1,(0,1,0,1):1,(0,0,1,2):1}
mo=10**9+7
def nb(tu):
    #print(tu)
    if not(tu in nd):
        if tu[tu[3]]==0:
            nd[tu] =0
        else:
            nt=list(tu)
            nt[tu[3]]-=1
            nt[3]=(nt[3]+1)%3
            nt2=nt[:]
            nt2[3]=(nt2[3]+1)%3
            nd[tu]=(tu[tu[3]]*(nb(tuple(nt))+nb(tuple(nt2))))%mo
    return nd[tu]

#print([(di[k],k[:3]) for k in di if k[3]==0])
print(sum(di[k]*(nb(k[:3]+(1,))+nb(k[:3]+(0,))+nb(k[:3]+(2,))) for k in di if k[3]==0)%mo)
#print(nd)
