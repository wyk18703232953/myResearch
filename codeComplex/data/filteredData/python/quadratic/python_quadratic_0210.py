from collections import defaultdict, deque
from heapq import heappush, heappop
from math import inf


def solve(n, m, res):
    cnt = defaultdict(int)
    for i in range(n):
        A = res[i]
        for j in range(m):
            if A[j]:
                cnt[j] += 1
    valid = False
    for r in res:
        j = [i for i in range(m) if r[i]]
        if all(cnt[i] > 1 for i in j):
            valid = True
            break
    if valid:
        print("YES")
    else:
        print("NO")


def main(n):
    if n <= 0:
        return
    # 定义矩阵规模：n 行，m 列
    m = max(1, n // 2)
    res = []
    for i in range(n):
        # 生成长度为 m 的 0/1 行，完全确定性
        row = [((i + j) % 3 == 0) for j in range(m)]
        res.append(row)
    solve(n, m, res)


if __name__ == "__main__":
    main(10)