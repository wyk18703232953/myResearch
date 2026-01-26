import sys
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def diff(s, x):
    if not s:
        return False
    return (max(s) - min(s)) >= x

def solve(problemset, l, r, x):
    multiset = powerset(problemset)
    cnt = 0
    for s in multiset:
        if not s:
            continue
        total = sum(s)
        if l <= total <= r and diff(s, x):
            cnt += 1
    return cnt

def main(n):
    if n < 1:
        n = 1
    l = n
    r = 2 * n
    x = max(1, n // 5)
    problemset = [i for i in range(1, n + 1)]
    result = solve(problemset, l, r, x)
    print(result)

if __name__ == "__main__":
    main(10)