from __future__ import division
from sys import stdin, stdout
from collections import Counter

def write(x):
    stdout.write(str(x) + "\n")


n, c = map(int, stdin.readline().split())
a = map(int, stdin.readline().split())
assert len(a) == n

tel = Counter()
target_count_last = Counter()
targets = 0
best = 0


for num in a:
    if num == c:
        targets += 1
    else:
        since_last = targets - target_count_last[num]
        target_count_last[num] = targets
        tel[num] = max(0, tel[num] - since_last)
        tel[num] += 1
        best = max(best, tel[num])

write(targets + best)
