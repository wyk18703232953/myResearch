n, pos, l, r=map(int, input().split())
if l==1 and r==n:
	print(0)
elif l==1 and r!=n:
	print(abs(pos-r)+1)
elif l!=1 and r==n:
	print(abs(pos-l)+1)
else:
	print(r-l+2+min(abs(pos-l), abs(pos-r)))