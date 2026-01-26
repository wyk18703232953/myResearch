from sys import stdin, stdout
n,m,k = [int(x) for x in stdin.readline().rstrip().split()]
L = [int(x) for x in stdin.readline().rstrip().split()]
off=1
page=-1
c=0
ans=0
for l in L:
    p=(l-off)//k
    if p==page:
        c+=1
    else:
        off+=c
        c=1
        ans+=1
        page=(l-off)//k
    
stdout.write( str(ans) + "\n" )