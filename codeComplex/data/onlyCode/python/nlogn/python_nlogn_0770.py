def fastio():
	import sys
	from io import StringIO 
	from atexit import register
	global input
	sys.stdin = StringIO(sys.stdin.read())
	input = lambda : sys.stdin.readline().rstrip('\r\n')
	sys.stdout = StringIO()
	register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
fastio()

MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

t, = I()
while t:
	t -= 1
	n, = I()
	a = I()
	a.sort()
	if n == 2:
		print(0)
	else:
		print(min(n-2, a[-2]-1))

