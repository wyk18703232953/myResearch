def subsets(S):
    sets = []
    len_S = len(S)
    for i in range(1 << len_S):
        subset = [S[bit] for bit in range(len_S) if i & (1 << bit)]
        sets.append(subset)
    return sets
    
n, l, r, x = list(map(int, input().split()))
problems = list(map(int, input().split()))
res = 0
for m in subsets(problems):
    if l <= sum(m) <= r and (max(m) - min(m)) >= x:
        res += 1
print(res)