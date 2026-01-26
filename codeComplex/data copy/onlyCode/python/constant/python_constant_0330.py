import sys
n=int(input())
if n==0:
	print(0)
	sys.exit()
if (n+1)%2==0:
	print((n+1)//2)
else:
	print(n+1)