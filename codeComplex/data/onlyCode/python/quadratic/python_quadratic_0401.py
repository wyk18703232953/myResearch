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
S = lambda: sys.stdin.readline().replace('\n', '').strip()
def grid(r, c): return [lint() for i in range(r)]
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')
star = lambda x: print(' '.join(map(str, x)))
localsys = 0
start_time = time.time()
if (path.exists('input.txt')):
	sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
#left shift --- num*(2**k) --(k - shift)

n , k= tup()
s = S()

fl =0
l = None
for i in range(1, n):
	x =s[i:n]
	for j in range(n):
		if x == s[:j+1]:
			l = j+1
			fl = 1
			break
	if fl :
		break
if fl :
	ans = s + s[l:n]*(k-1)
	print(ans)
else:
	print(s*k)






# n = I()
# ls = [int(i) for i in S()]
# pre , s =[] , 0
# for i in ls:
# 	s+=i
# 	pre.append(s)
# for i in range(n-1):
# 	cnt =0
# 	su =0
# 	for j in range(i+1 , n):
# 		su+=ls[j]
# 		if su == pre[i]:
# 			cnt+=1
# 			su =0
# 	if cnt and su ==0:
# 		print('YES')
# 		exit()
# print('NO')









if localsys:
	print("\n\nTime Elased :",time.time() - start_time,"seconds")
