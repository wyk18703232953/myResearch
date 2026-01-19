import sys,io,os,math
try:yash=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
except:yash=lambda:sys.stdin.readline().encode()
I=lambda:[*map(int,yash().split())]
import __pypy__;an=__pypy__.builders.StringBuilder()
n,=I();lis=I();N=22;dp=[-1]*(1<<22)
for i in range(n):
    dp[lis[i]]=lis[i]
    for j in range(22):
        lis[i]^=(1<<j)
for mask in range(1<<22):
    for i in range(22):
        if (mask&(1<<i)) and dp[mask^(1<<i)]!=-1:dp[mask]=dp[mask^(1<<i)]
for num in lis:
    an.append("%s "%(dp[num]))
an.append("\n")
os.write(1, an.build().encode())