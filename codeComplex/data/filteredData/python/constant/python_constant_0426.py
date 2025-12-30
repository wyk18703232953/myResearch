import random

def main(n: int):
    # 根据 n 生成测试数据，这里简单生成 m 为 1 到 2n 之间的随机数
    m = random.randint(1, 2 * n)
    print(f"n = {n}, m = {m}")

    if m <= n:
        print((m - 1) // 2)
    else:
        if (m - n) in range(1, n + 1):
            if (n - (m - n)) % 2 == 0:
                print((n - (m - n)) // 2)
            else:
                print((n - (m - n)) // 2 + 1)
        else:
            print(0)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)