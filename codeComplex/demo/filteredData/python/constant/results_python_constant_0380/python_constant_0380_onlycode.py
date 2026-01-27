a, b, c, n = map(int, input().split())
result = n - a - b + c
print(result if result > 0 and c <= a and c <= b else -1)