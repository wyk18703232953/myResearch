#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args,  file=sys.stderr)
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
    

import random
import time
random.seed( int(time.time()) )

bb = random.randint(0, 2**30-1)

hat1 = 0
hat2 = 0
lastresult = None
for i in range(29, -1, -1):
    g1 = hat1 + (1<<i)
    g2 = hat2 + (1<<i)
    
    if lastresult is None:
        print('?',hat1^ bb,hat2)
        t1 = int(input())
    else:
        t1 = lastresult
    if t1!=0:
        print('?',g1^ bb,g2)
        t2 = int(input())
        if t1!=t2:
            if t1==1:
                hat1+= (1<<i)
            else:
                hat2+= (1<<i)
            lastresult = None
            continue
    lastresult = t1
    print('?',g1^ bb,hat2)
    t3 = int(input())
    if t3==1:
        pass
    else:
        hat1+= (1<<i)
        hat2+= (1<<i)
    
print('!', hat1^bb% (2**30), hat2)



