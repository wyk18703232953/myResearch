import sys
lines = int(sys.stdin.readline())
dp = [0] * lines
f = 1
dp[0] = 1

for i in range(lines):
  char_in = sys.stdin.readline()[0]
  if char_in == 'f':
    f += 1
  else:
    # num ways to write the statements
    # the more for loops, the more we can combination
    # any single statement can be the indent of anything previously
    # sum over previous, but also update all of previous
    for j in range(1, f):
      dp[j] = (dp[j] + dp[j- 1]) % 1000000007
print(dp[f - 1])