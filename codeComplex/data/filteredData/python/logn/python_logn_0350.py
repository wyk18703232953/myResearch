import random

MOD = 1000000007
PHI_MOD = MOD - 1  # 1000000006


def helper(n: int) -> int:
    if n == 0:
        return 1
    p = 1
    ret = 2
    while n >= 2 * p:
        p *= 2
        ret = (ret * ret) % MOD
    return (ret * helper(n - p)) % MOD


def main(n: int) -> int:
    # 根据规模 n 生成测试数据：
    # x: 0 ~ MOD-1，k: 0 ~ n
    x = random.randrange(0, MOD)
    k = random.randrange(0, max(1, n))

    if x == 0:
        print(0)
        return 0

    x %= MOD
    k %= PHI_MOD

    a = helper(k)
    ans = (2 * a * x - a + 1) % MOD
    print(ans)
    return 0


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)