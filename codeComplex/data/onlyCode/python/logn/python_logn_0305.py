def mul(x, y, md):
	return x * y % md;

def power(x, y, md) :
	res = 1;
	while (y != 0):
		if (y & 1):
			res = mul(res, x, 1000000007);
		x = mul(x, x, 1000000007);
		y >>= 1;
	return res

def inv(x, md):
	return power(x, md - 2, 1000000007);

t = input().split()
a = int(t[0])
k = int(t[1])
if (a == 0):
	print(0)
else:
	first = power(2, 2 * k, 1000000007);
	second = power(2, k, 1000000007);
	ans = mul(first, 2 * a - 1, 1000000007) + second;
	third = inv(second, 1000000007);
	ans = mul(ans, third, 1000000007);
	print(ans)