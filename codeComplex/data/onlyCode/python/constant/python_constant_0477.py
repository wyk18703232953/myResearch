n, k = map(int, input().split())
h = k // n
if h * n < k:
    h += 1
print(h)
