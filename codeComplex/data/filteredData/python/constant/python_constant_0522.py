import random

def main(n: int):
    # n 为规模参数，这里用来控制随机数的范围
    # 生成测试数据：x, y, z, t1, t2, t3
    # 范围可根据 n 调整，这里简单设为 [-n, n] 或 [1, n]
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)
    t1 = random.randint(1, max(1, n))
    t2 = random.randint(1, max(1, n))
    t3 = random.randint(1, max(1, n))

    dp = abs(x - y) * t1
    dl = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3

    if dp < dl:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 可以自行修改 n 的默认值
    main(10)