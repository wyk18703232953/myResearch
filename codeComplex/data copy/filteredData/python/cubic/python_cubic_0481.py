import math
from collections import defaultdict, deque, OrderedDict
import bisect as bi

M = 998244353
P = 1000000007
Inf = float('inf')

def yes():
    # print('YES')
    pass

def no():
    # print('NO')
    pass

def find_gt(a, x):
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i

    else:
        return len(a)

def solve(n, m, k, rt, do):
    dp = [[0] * m for _ in range(n)]
    if k % 2 == 1:
        for i in range(n):
            # print(*[-1] * m)
            pass
        return
    k //= 2
    dp_next = [[P] * m for _ in range(n)]
    for _ in range(k):
        for i in range(n):
            for j in range(m):
                ans = Inf
                if i != 0:
                    ans = min(ans, dp[i - 1][j] + do[i - 1][j])
                if j != 0:
                    ans = min(ans, dp[i][j - 1] + rt[i][j - 1])
                if i != n - 1:
                    ans = min(ans, dp[i + 1][j] + do[i][j])
                if j != m - 1:
                    ans = min(ans, dp[i][j + 1] + rt[i][j])
                dp_next[i][j] = ans
        for i in range(n):
            for j in range(m):
                dp[i][j] = dp_next[i][j]
    for i in range(n):
        for j in range(m):
            # print(2 * dp[i][j], end=' ')
            pass
        # print()
        pass

def generate_data(n):
    # Map n to grid size and k deterministically
    # Let grid be roughly sqrt(n) x sqrt(n), and k depend on n
    if n <= 0:
        N = 1
        M_ = 1

    else:
        root = int(n ** 0.5)
        if root * root < n:
            root += 1
        N = max(1, root)
        M_ = max(1, root)
    K = (n % 10) * 2  # even k to avoid trivial -1 case for most n

    # Generate rt: N x (M_-1) horizontal edge weights, padded to M_ for simplicity
    rt = [[(i + j) % 7 + 1 for j in range(M_)] for i in range(N)]
    # Generate do: (N-1) x M_ vertical edge weights
    do = [[(i * 3 + j * 2) % 9 + 1 for j in range(M_)] for i in range(max(0, N - 1))]

    return N, M_, K, rt, do

def main(n):
    N, M_, K, rt, do = generate_data(n)
    solve(N, M_, K, rt, do)

if __name__ == "__main__":
    main(1000)