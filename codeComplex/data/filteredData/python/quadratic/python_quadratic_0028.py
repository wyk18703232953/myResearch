import random

mod = 10 ** 9 + 7


def summ(a, b):
    return (a + b) % mod


def main(n: int) -> int:
    # 1. 生成测试数据：长度为 n 的 'f' / 's' 序列
    #    True 表示为 'f'，False 表示为非 'f'（此处用 's'）
    #    如需可复现结果，可在调用前设置 random.seed(...)
    f = [random.choice([True, False]) for _ in range(n)]

    dp = [1]
    for ii in range(1, n):
        pf = f[ii - 1]
        if pf:
            dp.insert(0, 0)
        else:
            for jj in reversed(range(1, len(dp))):
                dp[jj - 1] = summ(dp[jj - 1], dp[jj])

    ans = 0
    for vv in dp:
        ans = summ(ans, vv)

    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：规模为 5 的测试
    main(5)