def get_path_hv(A, B):
	x, y = A

	path = [(x, y)]

	while x < B[0]:
		x += 1
		path.append((x, y))

	while x > B[0]:
		x -= 1
		path.append((x, y))

	while y < B[1]:
		y += 1
		path.append((x, y))

	while y > B[1]:
		y -= 1
		path.append((x, y))

	return path

def get_path_vh(A, B):
	x, y = A

	path = [(x, y)]

	while y < B[1]:
		y += 1
		path.append((x, y))

	while y > B[1]:
		y -= 1
		path.append((x, y))

	while x < B[0]:
		x += 1
		path.append((x, y))

	while x > B[0]:
		x -= 1
		path.append((x, y))

	return path

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

paths = []
paths.append([get_path_vh(A, B), get_path_hv(A, B)])
paths.append([get_path_vh(C, B), get_path_hv(C, B)])
paths.append([get_path_vh(A, C), get_path_hv(A, C)])

ans = 10 ** 8
ans_path = []

for i in range(3):
	for j in range(3):
		if i != j:
			for a in paths[i]:
				for b in paths[j]:
					X = list(set([*a, *b]))

					if len(X) < ans:
						ans = len(X)
						ans_path = X

print(ans)
for p in ans_path:
	print(*p)
