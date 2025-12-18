import sys
m,n=map(int,sys.stdin.readline().split())
res=m^n
s=bin(res)
s=s[2:]
s=int(s)
if(s==0):
    print(0)
else:
    s=str(s)
    res=(2**len(s))-1
    print(res)