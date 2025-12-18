# this is directly from: https://codeforces.com/contest/908/submission/46821547
# you can disregard this answer if desired

n, r = map(int, input().split())
y = []
x = list(map(int, input().split()))
for xi in x:
    yi = r
    for tx, ty in zip(x, y):
        if xi - 2 * r <= tx <= xi + 2 * r:
            dy = (4.0 * r ** 2 - (tx - xi) ** 2) ** 0.5
            yi = max(yi, ty + dy)
    y.append(yi)
print(*y)

				  			 		 					   		   		 	