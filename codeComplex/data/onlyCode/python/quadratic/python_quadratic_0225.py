import sys


# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ans = float('inf')
for i in range(1, n-1):
    bef = aft = float('inf')
    for j in range(i):
        if a[j] < a[i]:
            bef = min(bef, b[j])
    for j in range(i, n):
        if a[i] < a[j]:
            aft = min(aft, b[j])
    ans = min(ans, b[i]+bef+aft)
print(-1 if ans > 10**9 else ans)




