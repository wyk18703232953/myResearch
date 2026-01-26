#import sys
#sys.setrecursionlimit(150000)

from collections import deque
from copy import deepcopy


m,n,k  = map(int,input().split())

horizon = []
for i in range(m):
    horizon.append( list(map(int,input().split()))  )
    
vertical = []
for i in range(m-1):
    vertical.append( list(map(int,input().split()))  )


if k%2==1:
    ans = [-1]*n
    for i in range(m):
        print(" ".join(map(str,ans)))
    exit()
        
direc = [[0,-1],[0,1],[1,0],[-1,0]]

ans = [[0 for j in range(n)] for i in range(m)]


for t in range(k//2):
    tempans = deepcopy(ans)
   
    for i in range(m):
        for j in range(n):
            ans[i][j] = 2147483647
            for d in range(4):
                neighi = i + direc[d][0]
                neighj = j + direc[d][1]
                if neighi<0 or neighi>=m or neighj<0 or neighj>=n: continue 
                base = tempans[neighi][neighj] 
                if d==0: base += 2 * horizon[neighi][neighj]
                if d==1: base += 2 * horizon[neighi][neighj-1]
                if d==2: base += 2 * vertical[neighi-1][neighj]
                if d==3: base += 2 * vertical[neighi][neighj]  
                ans[i][j] = min(ans[i][j],base)

#    print(ans)
  



for ele in ans:
    print(" ".join(map(str,ele)))

         
            
                
        

