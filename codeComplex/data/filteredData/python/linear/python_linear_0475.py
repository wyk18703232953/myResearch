import math
from collections import defaultdict

def solve(n, c, a):
    vis = [False] * (n + 1)
    ans = 0
    d = defaultdict(lambda: 0)
    cycleno = 0

    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            while not vis[cur]:
                d[cur] = cycleno
                vis[cur] = True
                cur = a[cur]
            if d[cur] == cycleno:
                min_ = c[cur]
                first = cur
                cur = a[cur]
                while first != cur:
                    min_ = min(c[cur], min_)
                    cur = a[cur]
                ans += min_
            cycleno += 1
    return ans

def main(n):
    # n: size of the permutation and cost array
    # Deterministic data generation:

    # costs c[1..n]; c[0] unused
    # Use a simple deterministic pattern, e.g., c[i] = (i * 3) % (n + 7) + 1
    c = [0] + [((i * 3) % (n + 7)) + 1 for i in range(1, n + 1)]

    # permutation a[1..n]; a[0] unused
    # Construct a deterministic permutation with mixed cycle structure
    # Example: a[i] = (2*i) mod n + 1 gives a permutation on {1..n}
    a = [0] + [((2 * i) % n) + 1 for i in range(1, n + 1)]

    result = solve(n, c, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)