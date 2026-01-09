def main(n):
    import math, itertools
    from collections import Counter, deque, defaultdict
    from bisect import bisect_left, bisect_right
    from heapq import heappop, heappush, heapify, nlargest
    from copy import deepcopy

    mod = 10**9 + 7
    INF = float('inf')

    # 映射：给定规模 n，构造 n, m 和数组 c
    # 令 m = 2 * n，并让 c 中每个 0..n-1 至少出现一次，其余按 (i % n) 填充
    orig_n = n
    m = 2 * orig_n if orig_n > 0 else 0

    # 生成 c（原来是 0-indexed 的输入）
    c = []
    if orig_n > 0:
        # 先让每个 0..n-1 出现一次
        c.extend(range(orig_n))
        # 其余位置用 i % n 填充，保持确定性
        for i in range(m - orig_n):
            c.append(i % orig_n)

    # 原始程序逻辑开始
    n_val = orig_n
    cnt = [0] * n_val
    for x in c:
        cnt[x] += 1

    result = min(cnt) if cnt else 0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)