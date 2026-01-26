import sys
LI=lambda:list(map(int, sys.stdin.readline().split()))
MI=lambda:map(int, sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())
# sys.stdin=open('input.txt')
# sys.stdout=open('output.txt', 'w')
# for _ in range(II()):
n=II()
s=SI()
c=set(s)
ln=[0]*n
for d in c:
	last=-1
	# print(d, end=' ')
	for i, v in enumerate(s):
		if v==d:
			last=i
		if last==-1:
			ln[i]=int(1e9)
		else:
			ln[i]=max(ln[i], i-last+1)
	# print(ln)
print(min(ln))