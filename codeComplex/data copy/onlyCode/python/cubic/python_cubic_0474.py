d4i=[0,-1,0,1]
d4j=[-1,0,1,0]

def main():
    
    n,m,k=readIntArr()
    horizontalEdges=[] # [i,j] represents [i,j] to [i,j+1]
    for _ in range(n):
        horizontalEdges.append(readIntArr())
    verticalEdges=[] # [i,j] represents [i,j] to [i+1,j]
    for _ in range(n-1):
        verticalEdges.append(readIntArr())
    
    if k%2==1: # impossible
        ans=makeArr(-1,[n,m])
    else:
        dp=makeArr(inf,[n,m,k//2+1]) # dp[i][j][nMoves] is the minimum possible boredom
        for i in range(n):
            for j in range(m):
                dp[i][j][0]=0
        for nM in range(1,k//2+1): # nM is nMoves
            for i in range(n):
                for j in range(m):
                    # move right
                    if j+1<m:
                        dp[i][j][nM]=min(dp[i][j][nM],
                                         dp[i][j+1][nM-1]+horizontalEdges[i][j])
                    # move left
                    if j-1>=0:
                        dp[i][j][nM]=min(dp[i][j][nM],
                                         dp[i][j-1][nM-1]+horizontalEdges[i][j-1])
                    # move down
                    if i+1<n:
                        dp[i][j][nM]=min(dp[i][j][nM],
                                         dp[i+1][j][nM-1]+verticalEdges[i][j])
                    # move up
                    if i-1>=0:
                        dp[i][j][nM]=min(dp[i][j][nM],
                                         dp[i-1][j][nM-1]+verticalEdges[i-1][j])
        ans=makeArr(0,[n,m])
        for i in range(n):
            for j in range(m):
                ans[i][j]=dp[i][j][k//2]*2
    
    multiLineArrayOfArraysPrint(ans)
    
    return

import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
 
def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]

def makeArr(defaultVal,dimensionArr): # eg. makeArr(0,[n,m])
    dv=defaultVal;da=dimensionArr
    if len(da)==1:return [dv for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(x,y):
    print('? {} {}'.format(x,y))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ans):
    print('! {}'.format(ans))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
MOD=998244353
 
 
for _abc in range(1):
    main()