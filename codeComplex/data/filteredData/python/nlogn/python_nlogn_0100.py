import random

def main(n: int):
    # 生成测试数据：
    # n: 元素个数
    # a, b: 随机划分参数，1 <= b < n
    a = random.randint(1, max(1, n - 1))
    b = random.randint(1, max(1, n - 1))

    # 随机生成 n 个正整数高度
    h = [random.randint(1, 10**6) for _ in range(n)]

    # 原逻辑
    h.sort()
    Vasya = h[:b]
    Petya = h[b:]
    if not Vasya or not Petya:
        # 按原题语义，b 应满足 1 <= b < n，这里防御性处理
        print(0)
        return
    print(Petya[0] - Vasya[-1])


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)