from math import sqrt

a, v = map(int, input().split())
l, d, w = map(int, input().split())

def findt(u, v, a, dist):
	front = (v*v-u*u)/(2*a)
	if front > dist:
		return (sqrt(u*u+2*a*dist)-u)/a
	return (v-u)/a + (dist-front)/v

def solve(a, v, l, d, w):
	if v <= w or 2*a*d <= w*w:
		return findt(0, v, a, l)
	after = findt(w, v, a, l-d)
	peak = sqrt(a*d + w*w/2)
	if peak > v:
		travel = (v*v-w*w/2)/a
		before = (2*v-w)/a + (d-travel)/v
	else:
		before = (2*peak-w)/a
	return before + after

print(f'{solve(a, v, l, d, w):.8f}')