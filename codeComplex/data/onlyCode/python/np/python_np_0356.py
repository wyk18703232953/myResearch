
def naiveSolve():
    
    
    
    return



def main():
    
    t=int(input())
    allans=[]
    for _ in range(t):
        n,m=readIntArr()
        grid=[]
        for __ in range(n):
            grid.append(readIntArr())
        columns=[]
        for col in range(m):
            temp=[grid[i][col] for i in range(n)]
            columns.append(temp)
        
        valCol=[] # (value, column)
        for i in range(n):
            for j in range(m):
                valCol.append((grid[i][j],j))
        valCol.sort(reverse=True)
        
        # try all possible shifts for top n columns
        topCols=set()
        for val,col in valCol:
            topCols.add(col)
            if len(topCols)==n:
                break
        
        # try all configurations
        m2=len(topCols)
        grid2=[[-1 for __ in range(m2)] for ___ in range(n)]
        topColsList=list(topCols)
        for j in range(m2):
            col=topColsList[j]
            for i in range(n):
                grid2[i][j]=grid[i][col]
        ans=-inf
        for mask in range(n**m2):
            grid3=[[-1 for __ in range(m2)] for ___ in range(n)]
            for col in range(m2):
                shift=mask%n
                for row in range(n):
                    grid3[row][col]=grid2[(shift+row)%n][col]
                mask//=n
            tempAns=0
            for row in range(n):
                maxx=-inf
                for col in range(m2):
                    maxx=max(maxx,grid3[row][col])
                tempAns+=maxx
            ans=max(ans,tempAns)
        allans.append(ans)
        
    multiLineArrayPrint(allans)
    
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
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(r):
    print('? {}'.format(r))
    sys.stdout.flush()
    return readIntArr()
 
def answerInteractive(adj,n):
    print('!')
    for u in range(1,n+1):
        for v in adj[u]:
            if v>u:
                print('{} {}'.format(u,v))
    sys.stdout.flush()
 
inf=float('inf')
MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()