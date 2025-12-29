import random

def main(n):
    # 生成测试数据：
    # n 为给定规模
    # m 在 [1, 2n] 区间内随机生成，避免 m=0
    # a, b 在 [1, 100] 区间内随机生成
    if n <= 0:
        return

    m = random.randint(1, 2 * n)
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    # 原逻辑
    if n % m == 0:
        print(0)
    else:
        k = n % m
        print(min(k * b, (m - k) * a)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次运行
    main(10)