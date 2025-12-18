
a, b, c, d, e, f, g, h = map(int, input().split(' '))
i, j, k, l, m, n, o, p = map(int, input().split(' '))

s1 = [[a, b], [c, d], [e, f], [g, h]]
s1.sort()
bleft = s1[0]
tr = s1[3]
u, v, w, x = bleft[0], bleft[1], tr[0], tr[1]


def check(xd, dx, u, v, w, x):
	return (u <= xd and xd <= w and v <= dx and dx <= x)

god = [(i+k+m+o)/4, (j+l+n+p)/4]
nani = 0
for moo in [[i, j], [k, l], [m, n], [o, p]]:
	if check(moo[0], moo[1], u, v, w, x):
		print("Yes")
		quit()

	
if check(god[0], god[1], u, v, w, x):
	nani += 1


i, j = i+j, i-j
k, l = k+l, k-l
m, n = m+n, m-n
o, p = o+p, o-p

a, b = a+b, a-b
c, d = c+d, c-d
e, f = e+f, e-f
g, h = g+h, g-h

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = i, j, k, l, m, n, o, p, a, b, c, d, e, f, g, h

s1 = [[a, b], [c, d], [e, f], [g, h]]
s1.sort()
bleft = s1[0]
tr = s1[3]
u, v, w, x = bleft[0], bleft[1], tr[0], tr[1]


def check(xd, dx, u, v, w, x):
	return (u <= xd and xd <= w and v <= dx and dx <= x)

god = [(i+k+m+o)/4, (j+l+n+p)/4]


for moo in [[i, j], [k, l], [m, n], [o, p]]:
	if check(moo[0], moo[1], u, v, w, x):
		print("Yes")
		quit()

if check(god[0], god[1], u, v, w, x):
	nani += 1
if nani == 2:
	print("Yes")
	quit()

print("No")