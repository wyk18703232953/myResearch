n=input()
if int(n)>0:
	print(n)
elif -9<=int(n)<=0:
	print(0)
else:
	a=(-int(n))//10
	b=((-int(n))//100)*10+int(n[-1])
	print(max(-a,-b))