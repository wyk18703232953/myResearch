import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[-1] == 1: ans = a[:-1] + [2]
else: ans = [1] + a[:-1]
print(*ans)
