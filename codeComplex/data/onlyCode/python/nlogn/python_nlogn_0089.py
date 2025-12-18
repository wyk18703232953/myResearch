# https://codeforces.com/problemset/problem/169/A

n, a, b = map(int, input().split())

h = sorted(map(int, input().split()))

print(h[b] - h[b-1])
