def get_input_list():
	return list(map(int, input().split()))

n = int(input())
l = get_input_list()
r = get_input_list()

a = [0 for _ in range(n)]
m = []
m_ = []
for i in range(n):
	m.append(l[i] + r[i])
	m_.append(l[i] + r[i])
m.sort()
ma = m[-1] + 1

for i in range(n):
	a[i] = ma - m_[i]

l_ = []
r_ = []
for i in range(n):
	c = 0
	d = 0
	for j in range(i+1):
		if a[j] > a[i]:
			c += 1
	for j in range(i,n):
		if a[j] > a[i]:
			d += 1
	l_.append(c)
	r_.append(d)
res = True
for i in range(n):
	if l[i] != l_[i] or r[i] != r_[i]:
		res = False
		break
if res:
	print("YES")
	for i in range(n):
		a[i] = str(a[i])
	print(" ".join(a))
else:
	print("NO")