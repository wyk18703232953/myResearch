def wins(mem, l, pos):
	# print(pos)
	if mem[pos] != 0:
		return mem[pos] == 1

	val = l[pos]

	lo = pos - val
	while lo >= 0:
		if l[lo] > val and not wins(mem, l, lo):
			mem[pos] = 1
			return True
		lo -= val

	hi = pos + val
	while hi < len(l):
		if l[hi] > val and not wins(mem, l, hi):
			mem[pos] = 1
			return True
		hi += val

	mem[pos] = 2
	return False



n = int(input())
l = list(map(int, raw_input().split()))

mem = [0 for i in range(n)]
ans = ""
for i in range(n):
	ans += "A" if wins(mem, l, i) else "B"

print(ans)
