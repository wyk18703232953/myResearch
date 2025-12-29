import random
from collections import defaultdict

def find_pair_with_threshold(l, n, m, x):
    s = set()
    d = defaultdict(int)
    pm = (1 << m) - 1  # bitmask with m bits set to 1

    for i in range(n):
        a = 0
        for j in range(m):
            if l[i][j] >= x:
                a |= (1 << j)
        d[a] = i
        s.add(a)

    s = list(s)
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i] | s[j]) == pm:
                return [d[s[i]] + 1, d[s[j]] + 1]
    return [-1, -1]


def solve(l, n, m):
    st = 0
    end = 10**9
    ans = (0, 0)
    while st <= end:
        mid = (st + end) // 2
        s = find_pair_with_threshold(l, n, m, mid)
        if s[0] != -1:
            ans = s
            st = mid + 1
        else:
            end = mid - 1
    return ans


def main(n):
    # n = scale parameter; derive matrix dimensions from n
    # Example: let number of rows = n, number of columns = max(1, min(20, n))
    rows = n
    cols = max(1, min(20, n))

    # Generate test data: matrix l[rows][cols] with values in [0, 1e9]
    l = [[random.randint(0, 10**9) for _ in range(cols)] for _ in range(rows)]

    ans = solve(l, rows, cols)
    print(ans[0], ans[1])


if __name__ == "__main__":
    # Example invocation with some default scale
    main(5)