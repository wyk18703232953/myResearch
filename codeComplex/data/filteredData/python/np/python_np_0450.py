import random
from array import array
from typing import Tuple


def main(n: int) -> None:
    # 规模 n: 行数；列数 m 也可由 n 派生
    # 这里设定 m = min(8, max(1, n))，保证按位枚举可行（原程序复杂度与 2^m 有关）
    m = min(8, max(1, n))

    # 随机生成测试数据：n 行 m 列的矩阵，元素范围 [0, 10^9]
    mat = [array('i', (random.randint(0, 10**9) for _ in range(m))) for _ in range(n)]

    bit = array('h', [1 << i for i in range(m)])
    max_bit = 1 << m
    fullbit = max_bit - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = array('i', [-1]) * max_bit
        for i in range(n):
            mask = 0
            for j in range(m):
                if mat[i][j] >= x:
                    mask |= bit[j]
            dp[mask] = i

        for i in range(max_bit):
            if dp[i] == -1:
                continue
            for j in range(i, max_bit):
                if dp[j] != -1 and (i | j) == fullbit:
                    return dp[i], dp[j]

        return -1, -1

    ok, ng = 0, 10**9 + 1
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
    # 示例：调用 main(5)
    main(5)