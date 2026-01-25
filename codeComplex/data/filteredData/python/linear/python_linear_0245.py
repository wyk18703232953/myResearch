from collections import Counter

def solve(n, ribbons):
	L = len(ribbons[0])
	a = [Counter(r).most_common(1)[0][1] for r in ribbons]

	r = sorted([(x, i) for i, x in enumerate(a)], reverse=True)

	if n == 1:
		c = Counter(a)
		if c[L - 1] == 1:
			for i in range(3):
				if a[i] == L - 1:
					return i
		if c[L - 1] > 1:
			return 3
		if c[L] + c[L - 2] == 1:
			for i in range(3):
				if a[i] == L or a[i] == L - 2:
					return i
		if c[L] + c[L - 2] > 1:
			return 3

	if r[1][0] == r[0][0]:
		return 3
	if r[1][0] + n >= L:
		return 3
	return r[0][1]


def generate_ribbons(n):
	# n 控制字符串长度 L，固定 3 条丝带
	if n <= 0:
		n = 1
	L = n

	chars = ['K', 'S', 'T']
	ribbons = []
	for i in range(3):
		# 确定性构造：位置 j 使用 (i + j) % 3 选择字符
		ribbon = ''.join(chars[(i + j) % 3] for j in range(L))
		ribbons.append(ribbon)
	return ribbons


def main(n):
	cats = ('Kuro', 'Shiro', 'Katie', 'Draw')
	ribbons = generate_ribbons(n)
	k = solve(n, ribbons)
	print(cats[k])


if __name__ == "__main__":
	# 示例：使用 n=10 作为规模参数
	main(10)