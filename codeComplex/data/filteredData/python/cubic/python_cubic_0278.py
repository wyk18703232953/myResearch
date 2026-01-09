import sys,bisect,string,math,time,functools,random,fractions
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
rep=range;R=range

def Golf():n,*t=map(int,open(0).read().split())
def I():raise RuntimeError("input disabled")
def S_():raise RuntimeError("input disabled")
def IS():raise RuntimeError("input disabled")
def LS():raise RuntimeError("input disabled")
def MI():raise RuntimeError("input disabled")
def LI():raise RuntimeError("input disabled")
def LI_():raise RuntimeError("input disabled")
def NI(n):raise RuntimeError("input disabled")
def NI_(n):raise RuntimeError("input disabled")
def StoLI():raise RuntimeError("input disabled")
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def RA():raise RuntimeError("input disabled")
def RLI(n=8,a=1,b=10):raise RuntimeError("random disabled")
def RI(a=1,b=10):raise RuntimeError("random disabled")

def Rtest(T):
    raise RuntimeError("input-based testing disabled")

def GI(V,E,ls=None,Directed=False,index=1):
    g=[[] for _ in range(V)]
    org_inp=[]
    if ls is None:
        raise RuntimeError("input disabled")
    FromStdin=False
    for i in range(E):
        inp=ls[i]
        if len(inp)==2:
            a,b=inp;c=1

        else:
            a,b,c=inp
        if index==1:
            a-=1;b-=1
        aa=(a,c);bb=(b,c);g[a].append(bb)
        if not Directed:g[b].append(aa)
    return g,org_inp

def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
    raise RuntimeError("input disabled")

def TI(n):return GI(n,n-1,ls=[[i+1,i+2] for i in range(n-1)])

def accum(ls):
    rt=[0]
    for i in ls:rt+=[rt[-1]+i]
    return rt

def bit_combination(n,base=2):
    rt=[]
    for tb in R(base**n):
        s=[tb//(base**bt)%base for bt in R(n)]
        rt+=[s]
    return rt

def gcd(x,y):
    if y==0:return x
    if x%y==0:return y
    while x%y!=0:
        x,y=y,x%y
    return y

def YN(x):print(['NO','YES'][x])
def Yn(x):print(['No','Yes'][x])
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)

mo=10**9+7
inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)]
EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
compas=dict(zip('WENS',FourNb))
cursol=dict(zip('LRUD',FourNb))
l_alp=string.ascii_lowercase

read=None
readline=None
input=lambda: (_ for _ in ()).throw(RuntimeError("input disabled"))

show_flg=False
show_flg=True

def core_solve(x,y,z,R,G,B):
    dp=[[[0]*(z+1) for _ in range(y+1)]for _ in range(x+1)]
    n=x+y+z
    for t in range(0,n+1,2):
        for i in range(x+1):
            for j in range(y+1):
                k=t-i-j
                if 0<=k<=z:
                    if i+1<=x and j+1<=y:
                        dp[i+1][j+1][k]=max(dp[i+1][j+1][k],dp[i][j][k]+R[i]*G[j])
                    if i+1<=x and k+1<=z:
                        dp[i+1][j][k+1]=max(dp[i+1][j][k+1],dp[i][j][k]+R[i]*B[k])
                    if j+1<=y and k+1<=z:
                        dp[i][j+1][k+1]=max(dp[i][j+1][k+1],dp[i][j][k]+G[j]*B[k])
    ans=0
    for i in range(x+1):
        if dp[i][y][z]>ans:ans=dp[i][y][z]
    for i in range(y+1):
        if dp[x][i][z]>ans:ans=dp[x][i][z]
    for i in range(z+1):
        if dp[x][y][i]>ans:ans=dp[x][y][i]
    return ans

def generate_data(n):
    # n 映射为三种颜色列表的长度和数值规模
    x = n//3
    y = n//3
    z = n - x - y
    # 生成确定性的递减序列
    R = list(range(2*x, 1*x, -1))[:x]
    G = list(range(3*y, 2*y, -1))[:y]
    B = list(range(4*z, 3*z, -1))[:z]
    return x,y,z,R,G,B

def main(n):
    x,y,z,R,G,B = generate_data(n)
    ans = core_solve(x,y,z,R,G,B)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)