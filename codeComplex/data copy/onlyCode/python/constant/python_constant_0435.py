import math
n, k = map(int, input().split())
if k % 2 == 1:
  mink = (k + 1) // 2
else:
  mink = k // 2 + 1
print(max(0, min(k - 1, n) - mink + 1))
