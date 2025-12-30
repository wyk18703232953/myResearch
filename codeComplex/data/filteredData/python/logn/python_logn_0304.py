import random

MOD = int(1e9 + 7)

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设定：
    # x 在 [0, 10^n] 范围内，k 在 [0, n] 范围内
    upper_x = 10 ** max(1, n)  # 避免 10^0 = 1 过小
    x = random.randint(0, upper_x)
    k = random.randint(0, max(1, n))

    if x == 0:
        print(0)
    else:
        ans = (x * pow(2, k + 1, MOD) - pow(2, k, MOD) + 1) % MOD
        print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 5 运行
    main(5)