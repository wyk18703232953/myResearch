def parse(line):
	i = 0
	while line[i].isalpha():
		i += 1
	i1 = i
	while i < len(line) and line[i].isdigit():
		i += 1
	return line[:i1], int(line[i1:i]), line[i:]

for _ in range(int(input())):
	a1, n1, rest = parse(input())
	if rest:
		_, n2, _ = parse(rest)
		a2 = ''
		while n2:
			r = (n2 - 1) % 26
			a2 = chr(r + ord('A')) + a2
			n2 = (n2 - r - 1) // 26
		print(a2 + str(n1))
	else:
		n2 = 0
		for c in a1:
			n2 = 26 * n2 + (ord(c) - ord('A') + 1)
		print(f'R{n1}C{n2}')
		

