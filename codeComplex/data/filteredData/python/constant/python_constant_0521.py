import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里理解为生成 n 组 (x, y, z, t1, t2, t3) 并逐组计算
    # 若只需要一组数据，可忽略 n，直接生成一次即可。
    results = []
    for _ in range(n):
        # 根据需要自定义数据范围
        x = random.randint(-10**4, 10**4)
        y = random.randint(-10**4, 10**4)
        z = random.randint(-10**4, 10**4)
        t1 = random.randint(1, 10**3)
        t2 = random.randint(1, 10**3)
        t3 = random.randint(1, 10**3)

        a = abs(x - y) * t1
        b = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3

        if b <= a:
            results.append("YES")
        else:
            results.append("NO")

    # 输出全部结果，每行一条
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：运行 main(5) 生成并判断 5 组测试数据
    main(5)