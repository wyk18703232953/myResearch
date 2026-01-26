M = 10 ** 9 + 7
x, k = map(int, input().split())
if x == 0: print(0); exit(0)
P = pow(2, k, M)
r = (P * x) % M - (0.5 * (-1 + P)) % M
print(int((2 * r + M) % M))
