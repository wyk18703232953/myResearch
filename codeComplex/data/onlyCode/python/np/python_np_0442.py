import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from collections import defaultdict as dd
I = lambda : list(map(int,input().split()))

n,m=I()
l=[]
an=-1;a=b=0
for _ in range(n):
	k=I()
	l.append(k+[_+1])
	if an<min(k):
		a=b=_+1
		an=min(k)
le=an;r=10**9+1
while le<r:
	md = (le+r)//2
	f=0;a1=a2=-1
	s=[0]*n
	for i in range(n):
		for j in range(m):
			if l[i][j]>=md:
				s[i]|=1<<j

	po=1<<m
	d=[0]*po
	for i in range(n):
		d[s[i]]=i+1
	for i in range(1,po):
		if d[i]:
			pp=i
			while pp:
				d[pp]=d[i]
				pp=(pp-1)&i
	if d[po-1]:
		f=1
		a1=a2=d[po-1]
	for i in range(1,po):
		if d[i] and d[(po-1)^i]:
			f=1
			a1 = d[i]
			a2 = d[(po-1)^i]
			break
	if f:
		le=md+1
		if md>an:
			a,b=a1,a2
			an=md
	else:
		r=md
print(a,b)