def my_pow(a, n, m):
	if n == 0:
		return 1
	ans = my_pow(a, n // 2, m)
	if n % 2 == 0:
		return ans * ans % m

	else:
		return (ans * ans * a) % m

def main(n):
	mod = 10**9 + 7
	# 确定性生成 x, k，随 n 规模变化
	x = n
	k = n // 2
	if x == 0:
		# print(0)
		pass

	else:
		x *= 2
		ans = (x - 1) * my_pow(2, k, mod) + 1
		ans %= mod
		ans += 2 * mod
		# print(ans % mod)
		pass
if __name__ == "__main__":
	main(10)