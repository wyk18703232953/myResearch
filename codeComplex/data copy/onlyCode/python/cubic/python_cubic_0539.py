a=input()
b=input()
na=len(a)
nb=len(b)
def fs(a,b):
	try:
		for i in range(a+1,len(b)):
			if b[a]>b[i]:
				ans=b[i]
				k=b.copy()
				k.pop(i)
				ans+="".join(k)
				return ans
		return False
	except:
		return False
if(na<nb):
	print("".join(sorted(list(a),reverse=True)))
else:
	if(a==b):
		print(a)
		
	else:
		l=sorted(list(a),reverse=True)
		l2=l.copy()
		ans1=""
		flag=0
		ans=[]
		for i in b:
			for j in range(len(l)):
				if i==l[j]:
					k=fs(j,l)
					if(k!=False):
						ans.append(ans1+fs(j,l))
					ans1+=l[j]
					l.pop(j)
					break
				if i>l[j]:
					ans1+=l[j]
					l.pop(j)
					flag=1
					break
			if(flag==1):
				break
		ans1+="".join(l)
		if(int(ans1)<=int(b)):
			print(ans1)
		else:
			for i in sorted([int(i) for i in ans],reverse=True):
				if(i<=int(b)):
					print(i)
					break