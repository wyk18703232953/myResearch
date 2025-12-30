import random

def main(n):
    # 生成测试数据：根据规模 n 生成 x,k
    # 这里让 x,k 与 n 同量级，且保证 x 可以为 0 的情况被覆盖
    random.seed(0)
    x = random.randint(0, 10 ** 6 + n)
    k = random.randint(0, 10 ** 6 + n)

    if x == 0:
        print(0)
        return

    mod = 10 ** 9 + 7
    a = ((x % mod) * pow(2, k + 1, mod)) % mod
    print((a - (pow(2, k, mod) - 1)) % mod)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(10)