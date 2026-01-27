n, m = map(int, input().split())
s = 0
while m:
    s += n // m
    n, m = m, n % m
print(s)