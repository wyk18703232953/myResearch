from sys import stdin,stdout
from collections import Counter
def ai(): return list(map(int, stdin.readline().split()))
def ei(): return map(int, stdin.readline().split())
def ip(): return  int(stdin.readline().strip())
def op(ans): return stdout.write(str(ans) + '\n') 

n = ip()
s = input()
t = input()
value = {}
li = []
res1 = 0
res2 =res3 = -1
for i in range(n):
	if s[i] != t[i]:
		value[t[i]] = i
		res1 += 1
		li.append(i)
p = sq = False
for i in li:
	if s[i] in value:
		p = True
		res2 = i+1
		f = value[s[i]]
		res3 = f+1
		if s[f] == t[i]:
			sq = True
			break
print(res1-(2 if sq else 1 if p else 0))
print(res2,res3)