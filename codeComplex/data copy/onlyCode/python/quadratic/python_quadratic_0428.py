from sys import stdin,stdout
def main():
	n=int(stdin.readline())
	s=stdin.readline()
	sum=0
	a=[]
	for v in s:
		if v!='0' and v!='\n':
			a.append(v)
	if not a and n>1:
		return 'YES'
	n=len(a)
	s=a
	for i in range(n-1):
		sum+=int(s[i])
		j=i+1
		check=1
		while j<n:
			temp=int(s[j])
			j+=1
			while j<n:
				if temp>=sum:
					break
				temp+=int(s[j])
				j+=1
			if sum!=temp:
				check=1
				break
		if sum!=temp:
			check=0
		if check:
			return 'YES'
	return 'NO'
print(main())

