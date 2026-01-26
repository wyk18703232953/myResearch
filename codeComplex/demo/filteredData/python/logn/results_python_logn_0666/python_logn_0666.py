from collections import defaultdict as dd, deque as dq
import math, string

MOD = 10**9+7

def solve(N, K):
    x = (-3 + math.sqrt(9 + 8 * (N + K))) // 2
    return int(x * (x + 1) // 2 - K)

def main(n):
    # 映射：n 作为“输入规模”，生成一组 (N, K)
    # 保证 N >= K >= 0，且随 n 规模增大
    N = n * n + 3 * n + 5
    K = n // 2
    ans = solve(N, K)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)