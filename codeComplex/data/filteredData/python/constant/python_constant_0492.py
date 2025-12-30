import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设定：
    # a, b 都在 1 到 n 之间随机生成
    a = random.randint(1, max(1, n))
    b = random.randint(1, max(1, n))

    # 原逻辑：输出 (b + a - 1) // a
    print((b + a - 1) // a)


if __name__ == "__main__":
    # 示例：可在此处指定规模 n 来运行
    main(10)