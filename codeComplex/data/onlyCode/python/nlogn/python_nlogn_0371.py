n, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
s = []
for a in A:
    if not s:
        s.append(a)
        continue
    while s:
        if a-K <= s[-1] < a:
            s.pop()
        else:
            break
    s.append(a)
print(len(s))
