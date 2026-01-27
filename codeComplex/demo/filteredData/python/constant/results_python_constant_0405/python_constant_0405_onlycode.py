l, r = [{'0': 1, 'X': 0}[c] for cc in zip(input(), input()) for c in cc], 0
for i in range(0, len(l) - 3, 2):
    s = 7 - sum(l[i:i + 4])
    if s < 5:
        r += 1
        l[i:i + s] = [0] * s
print(r)