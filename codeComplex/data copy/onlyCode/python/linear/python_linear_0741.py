from sys import stdin,stdout
def count(audrey,imba,banget):
    return((imba-audrey-1)%(banget-1))
 
n,q=map(int,input().split())
L=list(map(int,input().split()))
maxi=max(L)
indexmax=L.index(maxi)
P=[]
for i in range(indexmax):
    P.append((L[0],L[1]))
    if L[0]<L[1]:
        L.append(L.pop(0))
    else:
        L.append(L.pop(1))
Y=tuple(L[1:])
for p in range(q):
    m=int(stdin.readline())
    if m<=indexmax:
        print(str(P[m-1][0])+' '+str(P[m-1][1]))
    else:
        stdout.write(str(maxi)+' '+str(Y[count(indexmax,m,n)])+'\n')