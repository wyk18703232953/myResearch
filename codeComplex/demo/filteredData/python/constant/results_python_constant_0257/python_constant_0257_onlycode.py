n, pos, l, r = map(int, input().split())
result = abs(pos - l) + r - l + 2
if (l == 1):
    if (abs(pos - r) + 1 < result):
        result = abs(pos - r) + 1
if (r == n):
    if (abs(pos - l) + 1 < result):
        result = abs(pos - l) + 1
if (l == 1 and r == n):
    result = 0
if (abs(pos - r) + r - l + 2 < result):
    result = abs(pos - r) + r - l + 2
print(result)