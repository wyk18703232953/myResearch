
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log2, ceil
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from bisect import insort
from collections import Counter
from collections import deque
from heapq import heappush,heappop,heapify
from itertools import permutations,combinations
from itertools import accumulate as ac
mod = int(1e9)+7
#mod = 998244353
 
ip = lambda : int(stdin.readline())
inp = lambda: map(int,stdin.readline().split())
ips = lambda: stdin.readline().rstrip()
out = lambda x : stdout.write(str(x)+"\n")

t = 1
for _ in range(t):
    q = "? {} {}".format(0,0)
    print(q,flush = True)
    cond = ip()
    cur_a = 0
    cur_b = 0
    for i in range(29,-1,-1):
        xor = (1<<i)
        query_a = cur_a^xor
        query_b = cur_b^xor
        q = "? {} {}".format(query_a,query_b)
        print(q,flush = True)
        val = ip()
        if val != cond:
            if cond == -1 and val == 1:
                cur_b ^= xor
                query_a = cur_a
                query_b = cur_b
                q = "? {} {}".format(query_a,query_b)
                print(q,flush = True)
                val = ip()
                cond = val
            else:
                cur_a ^= xor
                query_a = cur_a
                query_b = cur_b
                q = "? {} {}".format(query_a,query_b)
                print(q,flush = True)
                val = ip()
                cond = val
        else:
            cond = val
            query_a = cur_a^xor
            query_b = cur_b
            q = "? {} {}".format(query_a,query_b)
            print(q,flush = True)
            val = ip()
            if val == -1:
                cur_a ^= xor
                cur_b ^= xor
            else:
                pass
    ans = "! {} {}".format(cur_a,cur_b)
    print(ans,flush = True)
    
        
        
        
        
        
        
        
        
        
    



    
                    
                
                
            
                
            
            
        
                
                
        
    
    
    
        
    
        
            
        
        
        
        
            
        
        
    
        
            
        
                
        
        
        
        
        
            
            
            
            
            
        
    
            
    
            
            
            
            
            
            
            
                
                
                


    
        
