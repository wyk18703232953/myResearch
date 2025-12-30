import random
from array import array


def main(n: int) -> None:
    # 生成测试数据：长度为 n 的整数数组 a
    # 可按需要修改数据范围
    a = [random.randint(1, 10) for _ in range(n)]

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

    print(dp[0][-1])


if __name__ == '__main__':
    # 示例：调用 main，规模 n 可自行设定
    main(5)