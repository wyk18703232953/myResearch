import random

def main(n: int):
    # 可选的尺码集合
    sizes = ["M", "S", "XS", "XXS", "XXXS", "L", "XL", "XXL", "XXXL"]

    # 生成测试数据：长度为 n 的 a、b，每个元素为随机尺码
    a = [random.choice(sizes) for _ in range(n)]
    b = [random.choice(sizes) for _ in range(n)]

    cost = 0
    for s in sizes:
        ca = a.count(s)
        cb = b.count(s)
        cost += ca - min(ca, cb)

    print(cost)


if __name__ == "__main__":
    # 示例：n = 10，可按需修改
    main(10)