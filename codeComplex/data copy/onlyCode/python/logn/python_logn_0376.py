x,k = map(int, input().split())
mod = 1000000007
flag = True
if x==0:
    flag=False
if flag:
    print((pow(2,k+1,mod)*x-pow(2,k,mod)+1+mod)%mod)
else:
    print(0)
