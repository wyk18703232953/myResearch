from collections import Counter
ts=Counter(''.join(reversed(t)) for t in input().split())
t0 = None
run = 0
ans = 3
for t, c in sorted(ts.items()):
    if t0 is None or t[0] != t0[0] or int(t[1]) != int(t0[1])+1:
        run = 0
    t0 = t
    run += 1
    ans = min(ans, 3-max(c,run))
for s in 'spm':
    for r in range(1, 10):
        if s+str(r-1) in ts and s+str(r+1) in ts:
            ans = min(ans, 1)
print(ans)
