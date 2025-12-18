import sys,io,os
try:Z=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
except:Z=lambda:sys.stdin.readline().encode()
Y=lambda:[*map(int,Z().split())]
n,m,k=Y();H=[Y()for i in range(n)];V=[Y()for i in range(n-1)]
if k&1:print('\n'.join(' '.join(['-1']*m)for i in range(n)));quit()
d=[0]*n*m
for _ in range(k//2):
    nd=[0]*n*m
    for x in range(n):
        for y in range(m):
            v=x*m+y;w=[]
            if x:w.append(d[v-m]+V[x-1][y])
            if y:w.append(d[v-1]+H[x][y-1])
            if x<n-1:w.append(d[v+m]+V[x][y])
            if y<m-1:w.append(d[v+1]+H[x][y])
            nd[v]=min(w)
    d=nd
print('\n'.join(' '.join(map(lambda x:str(2*x),d[i*m:i*m+m]))for i in range(n)))