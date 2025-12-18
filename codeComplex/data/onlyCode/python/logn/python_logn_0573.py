from math import log
k=int(input())
r=k
l=1
t=log(10)
while 1:
	m=(l+r)//2
	x=int(log(m)/t)
	d=((1-10**(x+1))//9) + (m+1)*(x+1)
	if 0<=(k-d)<=13:
		break
	elif d>k:
		r=m-1
	else:
		l=m+1
if m==1000:
	d+=1
if d==k:
	print(str(m)[-1])
	exit()
st=""
v=k-d
m+=1
for i in range(13):
	st+=str(m)
	m+=1
print(st[v-1])



	