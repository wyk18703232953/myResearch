def solve():
  l, r = map(int, input().split())
  if l==r:
    print(0)
    return
  mx = str(bin(l^r))
  x = len(mx[2:])
  print(2**x-1)
solve()