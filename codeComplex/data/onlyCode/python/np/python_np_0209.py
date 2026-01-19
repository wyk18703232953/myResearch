n, l, r, x = map(int, input().split())
C = sorted(list(map(int, input().split())))
ANS = 0
for i in range(2 ** n):
    s = bin(i)[2:]
    s = '0' * (n - len(s)) + s
    L = []
    for j in range(n):
        if s[j] == '1':
            L.append(C[j])
    if len(L) < 2 or not (l <= sum(L) <= r) or L[-1] - L[0] < x:
        continue
    ANS += 1
print(ANS)
