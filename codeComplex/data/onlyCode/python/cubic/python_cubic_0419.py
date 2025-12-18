from math import inf

if True:
    n,m,k = map(int,input().split())
    cosp = [[int(x) for x in input().split()]+[inf] for _ in range(n)]
    cosv = [[int(x) for x in input().split()]for _ in range(n-1)]+[[inf]*m]
    if k%2==1:
        for _ in range(n):
            print(*[-1]*m)
     
    else:    
        dp = [[0]*m for i in range(n)]
        xx,yy = [0,0,1,-1],[1,-1,0,0]
        for _ in range(k//2):
            dp1 = [[inf]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    for kk in range(4):
                        x1,y1 = i+xx[kk],j+yy[kk]
                        if kk < 2:
                            if kk==1:
                                edge = cosp[i][j-1]
                            else:
                                edge=cosp[i][j]
                        else:
                            if kk==3 :
                                edge = cosv[i-1][j]
                            else:
                                edge = cosv[i][j]
                        if edge != inf:
                            dp1[i][j] = min(dp1[i][j],2*edge+dp[x1][y1])
            dp = dp1[:]
        for i in dp:
            print(*i)