from os import path
import sys,time
# mod = int(1e9 + 7)
# import re
from math import ceil, floor,gcd,log,log2 ,factorial
from collections import * 
# from bisect import *
maxx = float('inf')
#----------------------------INPUT FUNCTIONS------------------------------------------#
I = lambda :int(sys.stdin.buffer.readline())
tup= lambda : map(int , sys.stdin.buffer.readline().split())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().strip('\n')
def grid(r, c): return [lint() for i in range(r)]
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')
star = lambda x: print(' '.join(map(str, x)))
localsys = 0
start_time = time.time()
if (path.exists('input.txt')):
	sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
#left shift --- num*(2**k) --(k - shift)
s=S()
ans = s.replace('1','')+'2'
t =  ans.find('2')
# print(ans,t)
print(ans[:t]+'1'*s.count('1')+ans[t:len(ans)-1])






if localsys:
	print("\n\nTime Elased :",time.time() - start_time,"seconds")
