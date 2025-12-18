a,b = list(map(int, input().split()))
# print(a)
# print(b)
x = a ^ b
# print(x)
ans = 1
while x > 0:
	# print(x)
	x //= 2
	ans *= 2

print(ans -1)