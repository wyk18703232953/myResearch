n, s = list(map(int, input().split()))

def sum_of_digits(n):
	ans = 0
	for c in str(n):
		ans += int(c)
	return ans
m = s + 10 - s%10

while m - sum_of_digits(m) < s:
	m += 10
if m <= n:
	print(n - m + 1)
else:
	print(0)
