import random
from array import array
from typing import Tuple


def solve_indices(mat, bit, fullbit, x: int) -> Tuple[int, int]:
    n = len(mat)
    m = len(bit)
    dp = {}
    for i in range(n):
        mask = 0
        row = mat[i]
        for j in range(m):
            if row[j] >= x:
                mask |= bit[j]
        dp[mask] = i

    keys = tuple(dp.keys())
    for i in range(len(keys)):
        for j in range(i, len(keys)):
            if keys[i] | keys[j] == fullbit:
                return dp[keys[i]], dp[keys[j]]

    return -1, -1


def main(n: int):
    # 生成测试数据
    # n: 行数
    # m: 列数，设为与 n 同规模（可根据需要调整）
    m = max(1, n)

    # 生成一个 n x m 的矩阵，元素为 0~10^9 之间的随机整数
    mat = [array('i', (random.randint(0, 10**9) for _ in range(m))) for _ in range(n)]

    bit = [1 << i for i in range(m)]
    fullbit = (1 << m) - 1

    ok, ng = 0, 10**9 + 1
    ans_i, ans_j = 1, 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        x, y = solve_indices(mat, bit, fullbit, mid)
        if x == -1:
            ng = mid
        else:
            ok = mid
            ans_i, ans_j = x + 1, y + 1

    print(ans_i, ans_j)


if __name__ == '__main__':
    # 示例：规模 n = 5
    main(5)