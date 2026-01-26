import sys
a = list(map(int, sys.stdin.readlines()[1][:-1].split()))
mx = 0
for i in range(len(a)):
	if a[i] > mx:
		print(i+1)
		sys.exit(0)
	mx = max(mx,a[i] + 1)
print(-1)