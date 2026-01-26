
inp = input().split()
totNums, mod = int(inp[0]), int(inp[1])

def Exp(b,exp):
	if exp==0: return 1
	temp = Exp(b,exp>>1)**2
	if exp%2==1: temp*=b
	return temp%mod


#main
n = 410


#Precompute
fact, inv = [0 for i in range(n)],[0 for i in range(n)]
fact[0] = inv[0] = 1;
for i in range(1,totNums+1):
	fact[i] = fact[i-1]*i%mod
	inv[i] = Exp(fact[i],mod-2)

dp, choose = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]
for i in range(0,totNums+1):
	for j in range(0,i+1):
		choose[i][j] = fact[i]*inv[j]*inv[i-j]%mod
pow2 = [Exp(2,i) for i in range(n)]

#dp
dp[0][0] = 1
for i in range(totNums):
	for j in range(i+1):
		for k in range(1,totNums-i+1):
			dp[i+k+1][j+k] += dp[i][j]*pow2[k-1]*choose[j+k][k]
			dp[i+k+1][j+k] %= mod

ans = 0
for i in range(0,totNums+1):
	ans = (ans+dp[totNums+1][i])%mod
print(ans)