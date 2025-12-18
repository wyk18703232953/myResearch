
k={}
s=0

for i in range(int(input())):
	a,x=map(int,input().split())
	k[a]=x
	
for j in range(int(input())):
	b,y=map(int,input().split())
	if b in k:
		k[b]=max(k[b],y)
		# print(k[b])
	else:
		k[b]=y
s=0
for h in k.values():

	s+=h
print(s)

