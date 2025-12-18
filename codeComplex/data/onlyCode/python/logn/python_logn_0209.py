n, s = map(int,input().split())

def digs(k):
	r = k
	while k:
		r -= k % 10
		k //= 10
	return r
x = s + 19*9
while digs(x-1) >= s:
	x -= 1
print(max(n - x + 1, 0))