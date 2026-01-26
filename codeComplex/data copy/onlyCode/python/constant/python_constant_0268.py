n, pos, l, r = map(int,input().split())
step, dif = 0, lambda a, b : abs(a - b)

if dif(pos, l) < dif(pos, r):
	if l != 1:
		step += dif(pos, l) + 1
		pos = l
	if r != n:
		step += dif(pos, r) + 1
else:
	if r != n:
		step += dif(pos, r) + 1
		pos = r
	if l != 1:
		step += dif(pos, l) + 1
print(step)
