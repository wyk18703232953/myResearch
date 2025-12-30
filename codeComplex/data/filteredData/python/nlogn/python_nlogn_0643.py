import random

def main(n):
    # 生成测试数据：
    # n: 原代码中的 n
    # 随机设定 m 的规模，这里取 m = n（可按需要调整）
    m = n

    # 生成 x 数组（原本通过 n 行 input 读入）
    # 生成 n 个随机整数
    x = [0] * (n + 1)
    for i in range(n):
        x[i] = random.randint(1, 10**9 - 1)
    x[n] = 10**9  # 保持与原程序一致

    # 生成 m 个三元组 (x1, x2, y)（原本通过 m 行 input 读入）
    # 仅在 x1 == 1 时会使用 x2，y 完全未使用
    vert = []
    for _ in range(m):
        x1 = random.randint(1, 2)     # 只需 1 或 2 即可，表示是否加入 vert
        x2 = random.randint(1, 10**9)
        y = random.randint(1, 10**9)  # 虽然未使用，但保留形式
        if x1 == 1:
            vert.append(x2)

    # 以下逻辑与原程序一致
    vert.sort()
    x.sort()
    cur = 0
    minicount = n + m
    k = len(vert)
    for i in range(n + 1):
        while cur < k:
            if x[i] <= vert[cur]:
                break
            cur += 1
        minicount = min(minicount, k - cur + i)

    print(minicount)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)