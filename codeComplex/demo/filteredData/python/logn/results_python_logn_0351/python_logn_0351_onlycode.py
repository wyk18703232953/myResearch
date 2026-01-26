import math
mod=10**9 + 7

def calcpower(num,power,mod):    
    """
    raises the num to the power power
    """
    if(power==0):
        return 1
    
    a=[num,]
    temp=num
    for i in range(int(math.log(power,2))):
        #print(time.time()-ini,i)
        #print(temp)
        temp*=temp
        temp=temp%mod
        a.append(temp%mod)
    #print(a)
    #print(time.time()-ini)
    power=bin(power)[2:]
    
    power=power[::-1]
    res=1
    for i in range(len(power)):
        if(int(power[i])):
            res=(res*a[i])%mod
    return res%mod
import sys

x,k=map(int,input().split())

if(x==0):
    print(0)
    sys.exit()
if(k==0):
    print(2*x%mod)
    sys.exit()
ans=(2*x-1)*calcpower(2,k,mod)+1
#print(calcpower(2,k,mod))
print(ans%mod)