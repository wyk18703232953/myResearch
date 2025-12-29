import random

def main(n: int):
    # 生成测试数据：k 取 1..n 之间的随机正整数（避免除零）
    if n <= 0:
        raise ValueError("n must be positive")

    k = random.randint(1, n)

    # 原逻辑
    ans = (n * 2 + k - 1) // k + (n * 5 + k - 1) // k + (n * 8 + k - 1) // k
    print(ans)


if __name__ == "__main__":
    # 示例：自己指定规模 n
    main(10)