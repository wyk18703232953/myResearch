from sys import stdin,stdout
from math import ceil,log
def main():
	d={}
	n=int(stdin.readline())
	a=list(map(int,stdin.readline().split( )))
	m=-1;mm=10**10
	for v in a:
		if v not in d:
			d[v]=1
		else:
			d[v]+=1
		m=max(m,v)
		mm=min(mm,v)
	ans=0
	
	for v in a:
		
		exponent=ceil(log(v,2))
		power=2**exponent
		find=0
		while power-v>=0:
			if power-v>mm and power-v>m:
				break
			
			element=power-v
			if element in d and element==v and d[element]>1:
				find=1
				break
			elif element in d and element!=v:
				find=1
				break
			power=power*2
		if find==0:
			ans+=1
	stdout.write("%d\n"%(ans))

main()