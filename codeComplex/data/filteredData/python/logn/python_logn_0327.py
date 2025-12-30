import random

MOD = 1000000007

def main(n):
    # 根据规模 n 生成测试数据：
    # 让 k 与 n 相关，使得规模可控，这里简单设为 n
    # x 在 [0, 10^6] 之间随机生成
    random.seed(0)  # 固定种子，保证可复现
    x = random.randint(0, 10**6)
    k = n

    if x == 0:
        print(0)
    else:
        u = (pow(2, k, MOD) * (2 * x - 1) + 1) % MOD
        print(int(u))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)