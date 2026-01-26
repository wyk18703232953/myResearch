import collections, bisect
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cs = collections.Counter(arr)
print(min(cs[x] for x in range(1, n + 1)))
