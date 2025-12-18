import math

s = input()
t = input()
p1, p2, m1, m2, q = 0, 0, 0, 0, 0
for i in s:
 if i == '+':
  p1 += 1
 else:
  m1 += 1
for i in t:
 if i == '+':
  p2 += 1
 elif i == '-':
  m2 += 1
 else:
  q += 1
dp, dm = p1 - p2, m1 - m2
if dp < 0 or dm < 0:
 print(0.0)
else:
 ans = (math.factorial(q) / (math.factorial(dp) * math.factorial(dm))) / math.pow(2, q)
 print(ans)