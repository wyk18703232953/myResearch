import sys
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
t = 0
for i in range(1,n):
	t += a[i]==a[i-1]
if t >= 2:
	print("cslnb")
	sys.exit(0)
if t:
	for i in range(n):
		if a[i]==a[i+1]:
			if a[i] and a[i]!=a[i-1]+1:
				a[i] -= 1
				break
			else:
				print("cslnb")
				sys.exit(0)
print(["cslnb","sjfnb"][(sum(a)-t-n*(n-1)//2)&1])
	 	     		  	 	  			 	  		  			