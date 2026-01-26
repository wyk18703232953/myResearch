import sys

f = sys.stdin

def line():
    return f.readline().strip().split()

def powers(limit):
    size = limit+1
    p = [1]*size
    for n in range(1,size):
        p[n] = 2*p[n-1] % M
        
    return p

def binomials(limit):
    size = limit+1
    bc = [[0 for k in range(size)] for n in range(size)]
    for n in range(size):
        bc[n][0]=1
    
    for n in range(1,size):
        for k in range(1,n+1):
            bc[n][k] = bc[n-1][k-1] + bc[n-1][k]
            bc[n][k] %= M
    
    return bc

def solve():
    
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0]=1
    
    for i in range(1,N):
        for k in range(1,i):
            for j in range(1,i):
                dp[i][j] += BC[j+1][i-k] * dp[k-1][j-1-(i-k-1)] * POW[i-k-1]
                dp[i][j] %= M
        dp[i][i] = POW[i]

    res=0
    for j in range(0,N):
        res = (res + dp[N-1][j]) % M

    return str(res)

T = 1
for test in range(1,T+1):
    N,M = map(int,line())
    
    BC = binomials(N)
    POW = powers(N)
    
    print(solve())
    
f.close()