import sys
input = sys.stdin.readline

class sieve:
  def __init__(self, n):
    self.n = n
    self.sv = [1] * (n + 1)
    self.sv[0] = 0
    self.sv[1] = 0
    for i in range(2, n + 1):
      if self.sv[i]:
        for j in range(i * 2, n + 1, i):
          self.sv[j] = 0
  def isprime(self, x):
    if x > self.n:
      return False
    return self.sv[x] == 1
  def factorize(self, x):
    res = []
    for i in range(2, int(x ** 0.5) + 1):
      if self.sv[i]:
        while x % i == 0:
          x //= i
          res.append(i)
    if x != 1:
      res.append(x)
    return res
  def modlcm(self, a, mod):
    res = [0] * (self.n + 1)
    ex = set()
    for i in range(len(a)):
      f = self.factorize(a[i])
      for j in f:
        if j > self.n:
          ex.add(j)
          continue
        res[j] = max(f.count(j), res[j])
    rres = 1
    for i in range(self.n + 1):
      if res[i] != 0:
        rres *= pow(i, res[i], mod)
        rres %= mod
    for i in ex:
      rres *= i
      rres %= mod
    return rres

sv = sieve(10 ** 4)
for _ in range(int(input())):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  for i in range(n):
    x = a[i]
    q = sv.factorize(x)
    s = [1]
    while len(q):
      y = q.pop()
      if y == s[-1]:
        s.pop()
        a[i] //= y ** 2
      else: s.append(y)
  s = [set() for _ in range(k + 1)]
  #print(a)
  dp = [n] * (k + 1)
  dp[0] = 0

  for i in range(n):
    for j in range(k, -1, -1):
      if dp[j] == n: continue
      if a[i] in s[j]:
        if j + 1 <= k and dp[j + 1] > dp[j]:
          dp[j + 1] = dp[j]
          s[j + 1] = s[j]
        dp[j] += 1
        s[j] = set()
        s[j].add(a[i])
      else:
        s[j].add(a[i])
      

    #print(dp, s)

  for j in range(k + 1): dp[j] += len(s[j]) > 0
  print(min(dp))
