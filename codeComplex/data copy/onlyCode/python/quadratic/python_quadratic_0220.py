import sys
n=int(input())
#n=5
#l=[2,4,5,4,10]
#c=[40,30,20,10,40]
l=list(map(int,input().split()))
c=list(map(int,input().split()))
a=[]
for i in range(1,n-1):
    lr=sys.maxsize
    lc=sys.maxsize
    for j in range(0,i):
        
        if l[i]>l[j]:
            lc=min(lc,c[j])
            #print(lc,l[i])
    for j in range(i+1,n):
        
        if l[j]>l[i]:
            lr=min(lr,c[j])
            #print(lr,l[i])
    if lr<sys.maxsize and lc<sys.maxsize:
        a.append(lr+lc+c[i])
#print(a)
if not a:
    print(-1)
else:
    print(min(a))       
            
            