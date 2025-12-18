import math
def maxXor(l, r):
  if l == r:
    return 0
  xor = l ^ r
  twoPows = math.log(xor, 2)
  return 2 ** int(math.floor(twoPows) + 1) - 1

l, r = map(int, input().split())
print(maxXor(l, r))
