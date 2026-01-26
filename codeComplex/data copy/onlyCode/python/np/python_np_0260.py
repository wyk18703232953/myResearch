a,b,c,d,e,f=map(int,input().split())
if a<b:a,b=b,a
if c<d:c,d=d,c
if e<f:e,f=f,e
sides=[[a,b,'A'],[c,d,'B'],[e,f,'C']]
sides.sort(reverse=True)
c1,c2,c3=sides[0][2],sides[1][2],sides[2][2]
area=a*b+c*d+e*f
if int(area**0.5)**2!=area:
	print(-1)
else:
	l=int(area**0.5)
	if l not in sides[0]:
		print(-1)
	elif l in sides[1] and l in sides[2]:
		print(l)
		for i in range(3):sides[i].remove(l)
		for i in range(3):
			for _ in range(sides[i][0]):
				print([c1,c2,c3][i]*l)
	else:
		r=l-sides[0][1]
		if r in sides[1] and r in sides[2]:
			print(l)
			for i in range(1,3):sides[i].remove(r)
			for _ in range(sides[0][1]):
				print(c1*l)
			for _ in range(r):
				print(c2*sides[1][0]+c3*sides[2][0])
		else:
			print(-1)