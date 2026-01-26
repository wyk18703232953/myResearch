# your code goes here
MOD = 1000000007
def modpow(x, p):
    
    result = 1
    while p > 0:
        
        if p % 2 == 1:
            result = (result * x) % MOD

        
        p = p // 2
       
        x = (x * x) % MOD

    return result

n, k = map(int, input().split())
k+=1
if n == 0:
	print(0)
else:
	
	ans =  (((modpow(2, k))*(n%MOD))%MOD-(modpow(2, k-1)-1)%MOD)%MOD
	print(ans)