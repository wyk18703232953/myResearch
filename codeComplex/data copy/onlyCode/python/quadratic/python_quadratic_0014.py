R = lambda: map(int, input().split())

n, r = R()
xs = list(R())
ys = []
for i in range(n):
    ys.append(max([((2 * r) ** 2 - abs(xs[i] - xs[j]) ** 2) ** 0.5 + ys[j] for j in range(i) if abs(xs[i] - xs[j]) <= 2 * r], default=r))
print(*ys)