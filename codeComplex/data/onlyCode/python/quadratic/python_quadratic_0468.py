#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
    dprint('debug mode')
except Exception:
    def dprint(*args, **kwargs):
        pass



inId = 0
outId = 0
if inId>0:
    dprint('use input', inId)
    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #标准输出重定向至文件
if outId>0:
    dprint('use output', outId)
    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #标准输出重定向至文件
    atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit
    
N, = getIntList()
#print(N)

zl = getIntList()
zr = getIntList()

zt = [ (zl[i] + zr[i], i) for i in range(N) ]
zt.sort()
za = [0 for i in range(N) ]
now = N
for i in range(N):
    if i>0 and zt[i-1][0] <zt[i][0]:
        now-=1
    za[ zt[i][1] ] = now

for i in range(N):
    l = 0
    r = 0
    for j in range(i):
        if za[j] > za[i]:
            l+=1
    for j in range(i+1, N):
        if za[j] > za[i]:
            r+=1
    if zl[i] != l or zr[i] != r:
        print('NO')
        sys.exit()
print('YES')
for i in range(N):
    print(za[i],end = ' ')




