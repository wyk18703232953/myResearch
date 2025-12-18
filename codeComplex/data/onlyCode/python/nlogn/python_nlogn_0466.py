n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(a)
b.sort()
c=[]
sum=0
for i in range(1,k+1):
	c.append(b[-i])
	sum+=b[-i]
print(sum)
d=[]
for i in range(n):
	if a[i] in c:
		d.append(i)
		c.remove(a[i])
	else:
		pass
d.insert(0,-1)
d[-1]=n-1
e=[]
for i in range(1,len(d)):
    e.append(d[i]-d[i-1])
print(" ".join(map(str,e)))