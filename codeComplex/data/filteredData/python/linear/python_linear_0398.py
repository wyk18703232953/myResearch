import random

MOD = 998244353

def main(n: int):
    # 1. 生成规模为 n 的测试数据 a
    # 根据需要可调整数据范围
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 2. 原逻辑
    s = a[0] % MOD
    y = a[0]
    for x in a[1:]:
        s = s * 2 + y + x
        y = y * 2 + x
        s %= MOD
        y %= MOD

    print(s)


if __name__ == "__main__":
    # 示例：可修改此处测试不同规模
    main(5)