#Python is love <3
def ii():
    return int(input())
def mi():
    return map(int,input().split())
def li():
    return list(map(int,input().split()))

mod = 10**9 + 7

x,k = mi()
if(x == 0):
    print(0)
elif(k == 0):
    print((2*x)%mod)
else:
    to = pow(2,k,mod)
    pre = (to * x)%mod
    prev = pow(2,k-1,mod)
    first = (pre - prev + 1)%mod
    sec = (pre - prev)%mod
    ans = (first + sec)%mod
    print((ans+mod)%mod)