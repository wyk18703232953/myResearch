a = int(input())
s = input()
d = s.count('H')
p = []
for i in range(len(s)):
	if i+d > len(s):
		n = d+i - len(s)
		m = d - n
		h = s[:m] + s[-n:]
		k = h.count("T")
		p.append(k)
	else:
		h = s[i:d+i]
		k = h.count("T")
		p.append(k)
mi = a
for i in range(len(p)):
	if p[i] < mi:
		mi = p[i]
if s.count("H") == 1 or s.count("T") == 0:
	print(0)
else:
	print(mi)

