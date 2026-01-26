def f(a,b):
	r=list(bin(b).lstrip("0b"))
	l=list((len(bin(b))-len(bin(a)))*("0")+bin(a).lstrip("0b"))
	for i in range(len(r)):
		if (r[i]=="1" and l[i]=="1"):
			r[i]="0"
			if int("".join(r),2)>=a:
				pass
			else:
				r[i]="1"
		if l[i]=="0" and r[i]=="0":
			l[i]="1"
			if int("".join(l),2)<=b:
				pass
			else:
				l[i]="0"
	l=int("".join(l),2)
	r=int("".join(r),2)
	return l^r



a,b=map(int,input().strip().split())
print(f(a,b))