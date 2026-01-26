n, k = map(int, input().split())

def prod(n):
	if n%2:
		return n*((n+1)//2)
	else:
		return (n//2)*(n+1)

def total_count(n, k):
	if k >= n:
		return (0, 0, 1)
	else:
		count = 0
		l = 1; r = k
		s = prod(k)
		while l <= r:
			mid = (l+r)//2
			if n > s - prod(mid) + mid:
				r = mid-1
			else:
				l = mid+1

		n = n - (s - prod(l) + l)
		count += (k-l+1)
		k = l-1
		return (n, k, count)		

if prod(k) - (k-1) < n:
	print(-1)
elif n == 1:
	print(0)
elif k >= n:
	print(1)
else:
	n = n-k
	k = k-2
	count = 1
	while n > 0:
		(n, k, temp) = total_count(n, k)
		count += temp
	print(count)