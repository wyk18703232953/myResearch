import math,io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# sys.stdout.write(str(x) + "\n")

n,s=map(int,input().split())
c=0
i=n
for i in range(s,min(s+1000,n+1)):
    if i-sum(map(int,str(i)))>=s:
        c+=1
c+=max(0,n-i)
print(c)
