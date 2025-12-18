import sys


N, M, K, L = map(int, sys.stdin.readline().split())

if M * (N / M) - K < L:
  print("-1")
  sys.exit(0)

def solve(curr):
  return curr * M - K >= L

l = 0
r = N / M
while r - l > 1:
  mid = (r + l) / 2
  if solve(mid):
    r = mid
  else:
    l = mid

print(r)
