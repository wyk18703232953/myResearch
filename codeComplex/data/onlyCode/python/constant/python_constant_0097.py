def solve(a, b):
    m = max(a, b)
    n = min(a, b)
    if n == 0:
        return 0
    if m == n:
        return 1
    elif m % n == 0:
        return m // n
    k = m // n
    return k + solve(n, m - n * k)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solve(a, b))