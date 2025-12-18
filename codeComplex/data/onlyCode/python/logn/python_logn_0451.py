# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import math
import heapq
from itertools import accumulate

Q = int(input())
#s = input() 
#N,K = [int(x) for x in stdin.readline().split()]

four = []

for i in range(62):
    four.append(4**i)

for i in range(Q):
    N,K = [int(x) for x in stdin.readline().split()]
    
    tmp_N = N
    if N>=60:
        N = 60
        
    dk = (4**(N)-1)//3
    if K>dk:
        print('NO')
        continue
    
    seq = []
    block = []
    s = 0
    for i in range(N):
        s += 2**(i+1) - 1
        block.append(2**(i+1)-1)
        seq.append(s)
        
    if K>=seq[-1]:
        print('YES',0)
        continue
    
    #print(seq)
    for i in range(N-1):
        if K>=seq[i] and K<seq[i+1]:
            d = K-seq[i]
            happy = tmp_N-i-1
            round = i+1
            break
    
    block = block[::-1]
    #print(block)
    res = 0
    for i in range(round):
        A = (4**(i+1)-1)//3
        B = block[i] - 2
        res += A*B
        
    #print(res)
    
    if d<=res:
        print('YES',happy)
    else:
        print('NO')
    
        
    
    
    
    
    