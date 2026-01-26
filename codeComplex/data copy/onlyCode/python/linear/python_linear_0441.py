ceil1 = lambda a, b: (a + b - 1) // b
n = int(input())
sq = int(n ** .5)
sq2, ans, cur = ceil1(n, sq), [], 0

for i in range(sq2 - 1):
    cur += sq
    ans.extend([x for x in range(cur, cur - sq, -1)])

ans.extend([x for x in range(n, cur, -1)])
print(' '.join(map(str, ans)))
