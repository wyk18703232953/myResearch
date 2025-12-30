def main(n):
    # 生成测试数据
    # 这里把原程序中的 m 设为 n，k 设为一个与 n 相关的值（例如 3 或 n//3+1）
    import random

    m = n
    k = max(1, n // 3)  # 保证 k >= 1
    # 生成递增的 p 数组，模拟原题中常见的“位置”或“编号”场景
    p = []
    cur = 0
    for _ in range(m):
        cur += random.randint(1, 3)  # 相邻差值为 1~3，保持有序
        p.append(cur)

    # 原始逻辑
    i = 0
    c = 0
    d = 0
    while i < m:
        c += 1
        d2 = d
        x = k * ((p[i] - d2 - 1) // k) + k
        while i < m and p[i] - d2 <= x:
            i += 1
            d += 1

    print(c)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)