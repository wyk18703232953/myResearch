import random
from array import array
from typing import Tuple


def main(n: int):
    # 产生规模为 n 的随机测试数据
    # 设定 m = min(n, 10) 以控制 2^m 的复杂度
    m = max(1, min(n, 10))
    # 随机数范围与原二分上界一致
    value_max = 10**9

    # 随机生成 n x m 矩阵
    mat = [
        array('i', (random.randint(0, value_max) for _ in range(m)))
        for _ in range(n)
    ]

    bit = [1 << i for i in range(m)]
    max_bit = 1 << m
    fullbit = max_bit - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = array('i', [-1]) * max_bit
        for i in range(n):
            mask = 0
            row = mat[i]
            for j, y in enumerate(row):
                if y >= x:
                    mask |= bit[j]
            dp[mask] = i

        for i in range(max_bit):
            if dp[i] == -1:
                continue
            for j in range(i, max_bit):
                if dp[j] != -1 and (i | j) == fullbit:
                    return dp[i], dp[j]
        return -1, -1

    ok, ng = 0, value_max + 1
    ans_i, ans_j = 1, 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        x, y = solve(mid)
        if x == -1:
            ng = mid
        else:
            ok = mid
            ans_i, ans_j = x + 1, y + 1

    print(ans_i, ans_j)


if __name__ == '__main__':
    # 示例：调用 main，规模 n 可自行修改
    main(5)