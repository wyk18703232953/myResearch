# import sys
# sys.stdin = open('CF_E93_D2/input.txt', 'r') 
# sys.stdout = open('CF_E93_D2/output.txt', 'w')
#----------------------------------------------------------------

r,g,b = list(map(int,input().split()))
dp = [ [ [-1]*(b+1) for i in range(g+1) ] for j in range(r+1) ]
ra = sorted(list(map(int,input().split())),reverse=True)
ga = sorted(list(map(int,input().split())),reverse=True)
ba = sorted(list(map(int,input().split())),reverse=True)

def solve(i,j,k) :
    
    if dp[i][j][k] != -1 :
        return dp[i][j][k]

    if i==r :
        if j==g or k==b :
            return 0
        dp[i][j][k] = ga[j] * ba[k] + solve(i,j+1,k+1)

    elif j==g :
        if i==r or k==b:
            return 0
        dp[i][j][k] = ra[i] * ba[k] + solve(i+1,j,k+1)
        
    elif k==b :
        if j==g or i==r:
            return 0
        dp[i][j][k] = ga[j] * ra[i] + solve(i+1,j+1,k)
    
    else :
        dp[i][j][k] = max(ra[i]*ga[j] + solve(i+1,j+1,k),ra[i]*ba[k] + solve(i+1,j,k+1),ba[k]*ga[j] + solve(i,j+1,k+1))

    return dp[i][j][k]


print(solve(0,0,0))