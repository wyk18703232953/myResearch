import sys, heapq

n = int(sys.stdin.readline())
key = []
for i in ['S', 'M', 'L']:
    for j in range(4):
        key.append(j * 'X' + i)
prev = dict().fromkeys(key, 0)
now = dict().fromkeys(key, 0)
for _ in range(n):
    prev[sys.stdin.readline().rstrip()] += 1
for _ in range(n):
    now[sys.stdin.readline().rstrip()] += 1
for i in key:
    temp = min(prev[i], now[i])
    prev[i] -= temp
    now[i] -= temp
ans = 0
for i in key:
    ans += now[i]
print(ans)

