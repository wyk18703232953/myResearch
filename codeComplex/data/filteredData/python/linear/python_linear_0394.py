import random

MOD = 998244353

def main(n):
    # 1. 生成规模为 n 的测试数据
    # 这里生成 n 个 [0, MOD-1] 范围内的随机整数
    a = [random.randrange(MOD) for _ in range(n)]

    # 2. 原逻辑计算
    difficulty = a[0] % MOD
    expectation = a[0] % MOD
    for i in range(1, n):
        expectation = expectation * 2 + difficulty + a[i]
        difficulty = difficulty * 2 + a[i]
        expectation %= MOD
        difficulty %= MOD

    # 3. 输出结果
    print(expectation)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)