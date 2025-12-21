def main(n):
    import sys
    from itertools import chain, combinations
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    def diff(s, x):
        return True if (max(s) - min(s)) >= x else False
    def solve(problemset, l, r, x):
        multiset = powerset(problemset)
        cnt = 0
        for s in multiset:
            if sum(s) >= l and sum(s) <= r and diff(s, x):
                cnt += 1
        return cnt
    sys.setrecursionlimit(10**7)
    problemset = list(range(1, n + 1))
    l = n
    r = n * (n + 1) // 2
    x = max(1, n // 2)
    return solve(problemset, l, r, x)
if __name__ == "__main__":
    print(main(4))