import sys
readline = sys.stdin.readline

k = list(map(int, readline().split()))


ans = 'NO'
if min(k) == 1 or k.count(2) >= 2 or k.count(3) >= 3 or (k.count(4) == 2 and k.count(2) == 1):
    ans = 'YES'

print(ans)