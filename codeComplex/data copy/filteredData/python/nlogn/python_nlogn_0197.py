def main(n):
	a = [(i * 2) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(n)]
	s = 0
	count = dict()
	for x in a:
		count[x] = count.get(x, 0) + 1
		s += x

	answer = 0
	for i in range(n):
		trash = 0
		trash += count.get(a[i] - 1, 0) * (a[i] - 1)
		trash += count.get(a[i], 0) * a[i]
		trash += count.get(a[i] + 1, 0) * (a[i] + 1)

		xcount = n - i
		xcount -= count.get(a[i] - 1, 0)
		xcount -= count.get(a[i], 0)
		xcount -= count.get(a[i] + 1, 0)

		answer += (s - trash) - (xcount * a[i])

		count[a[i]] -= 1
		s -= a[i]
	return answer

if __name__ == "__main__":
	# print(main(10))
	pass