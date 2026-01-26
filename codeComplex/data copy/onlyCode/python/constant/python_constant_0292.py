k, n, s, p = map(int, input().split())
L = (n - 1) // s + 1
L *= k
print((L - 1) // p + 1)