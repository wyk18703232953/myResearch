import sys
input = sys.stdin.readline

def readPair():
  return tuple(map(int, input().split()))

(n, m) = readPair()
entries = [readPair() for _ in range(0, n)]
entries.sort(key=lambda x: x[1] - x[0])

size = sum(x[0] for x in entries)
count = 0

while (size > m and count < n):
  size -= entries[count][0] - entries[count][1]
  count += 1

print(-1 if size > m else count)