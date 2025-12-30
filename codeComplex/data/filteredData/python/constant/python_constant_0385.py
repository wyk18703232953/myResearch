import random

def main(n: int):
    # 根据规模 n 生成测试数据 a, b, c, n_input
    # 这里将 n 作为上限，生成不大于 n 的随机整数
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, n)
    n_input = n  # 原程序中的 n

    p = a + b - c
    if p <= n_input - 1 and a - c >= 0 and b - c >= 0:
        print(n_input - p)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)