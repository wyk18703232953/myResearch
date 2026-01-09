import sys
from array import array  # noqa: F401
from typing import List, Tuple, TypeVar, Generic, Sequence, Union  # noqa: F401


def main(n: int):
    # n 表示数组 a 的长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成测试数据：a[i] = (i % 5)
    a = [i % 5 for i in range(n)]

    dp = [array('h', [10000]) * (n + 1) for _ in range(n + 1)]
    num = [array('h', [-1]) * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = 1
        num[i][i + 1] = a[i]

    for sublen in range(2, n + 1):
        for l, r in zip(range(n), range(sublen, n + 1)):
            for mid in range(l + 1, r):
                if num[l][mid] == num[mid][r] != -1:
                    dp[l][r] = 1
                    num[l][r] = num[l][mid] + 1
                    break

                dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid][r])

    # print(dp[0][-1])
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 进行规模化实验
    main(10)