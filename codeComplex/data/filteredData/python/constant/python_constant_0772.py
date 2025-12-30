import random

def main(n: int):
    # 生成测试组数 t，这里设为 n（也可以根据需要调整）
    t = n

    for _ in range(t):
        # 对每组数据生成一个长度为 n 的数组 g
        # 数值范围可根据实际需要调整，这里设为 1 到 2n
        g = [random.randint(1, 2 * n) for _ in range(n)]

        # 原逻辑
        m1 = max(g)
        g.remove(m1)
        m2 = max(g)
        dl = len(g) - 1
        print(min(dl, m2 - 1))


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)