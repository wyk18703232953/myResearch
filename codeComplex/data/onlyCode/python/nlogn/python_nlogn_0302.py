import sys
import heapq
input = sys.stdin.readline
n = int(input())
w = [int(z) for z in input().split()]; s = input(); idx = []
for i in range(n):
    idx.append((w[i], i+1))

idx.sort()
heapq.heapify(idx)
ones = []
heapq.heapify(ones)
res = []
for i in range(2*n):
    if s[i] == '0':
        l = idx[0]
        heapq.heappop(idx)
        res.append(l[1])
        heapq.heappush(ones, [-l[0], l[1]])
    else:
        l = ones[0]
        heapq.heappop(ones)
        res.append(l[1])
res = ' '.join([str(i) for i in res])
sys.stdout.write(res)