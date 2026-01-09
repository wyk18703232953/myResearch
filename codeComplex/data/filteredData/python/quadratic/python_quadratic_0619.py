from math import *


def main(n: int):
    # 生成测试数据
    # 假设 m 和 k 与 n 同量级：m <= n，k 为常数或与 n 线性相关
    # 这里示例：m = max(1, n // 3)，k = max(1, n // 10)
    m = max(1, n // 3)
    k = max(1, n // 10)

    # 生成长度为 n 的整数序列 l，这里用简单模式：l[i] = (i % 7) - 3
    l = [(i % 7) - 3 for i in range(n)]

    a = [0 for _ in range(n + 1)]
    ans = 0

    for M in range(m):
        min1 = 0
        for i in range(1, n + 1):
            a[i] = a[i - 1] + l[i - 1]
            if i % m == M:
                a[i] -= k
                ans = max(ans, a[i] - min1)
            min1 = min(min1, a[i])
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例运行：可以在这里调整 n 观测规模变化
    main(10)