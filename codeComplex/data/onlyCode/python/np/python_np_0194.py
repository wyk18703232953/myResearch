[n, l, r, x] = list(map(int, input().strip().split()))
Cs = list(sorted(map(int, input().strip().split())))
probs = 0

for i in range(1, 2**n):
    currsub = [ Cs[j] for j in range(n) if (i & (1 << j))]
    probs += (len(currsub) > 1 and l <= sum(currsub) <= r and currsub[-1] - currsub[0] >= x)
    
print(probs)