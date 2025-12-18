import sys

n,a,b = map(int, sys.stdin.readline().strip().split(' '))

ans = []
g = {i:set({}) for i in range(n)}

if a > 1 and b > 1:
	print("NO")
elif a == 1 and b == 1:
	if n == 1:
		print("YES")
		print("0")
	elif n < 4:
		print("NO")
	else:
		for i in range(n-1):
			g[i].add(i+1)
			g[i+1].add(i) 
		for i in range(n):
			tmp = []
			for j in range(n):
				if i in g[j]:
					tmp.append('1')
				else:
					tmp.append('0')
			ans.append(''.join(tmp))
		print("YES")
		print('\n'.join(ans))
else:
	swap = False
	if a == 1:
		a, b = b, a
		swap = True
	for i in range(a-1,n-1):
		g[i].add(i+1)
		g[i+1].add(i) 
	if swap:
		for i in range(n):
			tmp = []
			for j in range(n):
				if i == j:
					tmp.append('0')
				elif i not in g[j]:
					tmp.append('1')
				else:
					tmp.append('0')
			ans.append(''.join(tmp))
	else:
		for i in range(n):
			tmp = []
			for j in range(n):
				if i in g[j]:
					tmp.append('1')
				else:
					tmp.append('0')
			ans.append(''.join(tmp))
	print("YES")
	print('\n'.join(ans))