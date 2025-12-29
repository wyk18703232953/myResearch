import random

def main(n: int):
    # 生成列数 m，这里简单设为 n，也可按需调整
    m = n

    # 生成测试数据 x：n 行 m 列的 0/1 矩阵
    # 保证至少一行满足条件：删除该行后每一列仍然有至少一个 1
    x = [[0] * m for _ in range(n)]

    # 先构造一行“关键行”，使得其他行的并集在所有列上都有 1
    # 简单策略：除了第 0 行外，其余行随机设置 0/1，直到每列至少有一个 1
    for i in range(1, n):
        for j in range(m):
            x[i][j] = random.randint(0, 1)

    # 确保每一列至少有一个 1（如果没有，则在第 1 行补 1）
    for j in range(m):
        if all(x[i][j] == 0 for i in range(1, n)):
            x[1][j] = 1

    # 现在其他行已经覆盖所有列，再生成第 0 行，可以随意（比如随机）
    for j in range(m):
        x[0][j] = random.randint(0, 1)

    # 下面是原逻辑：判断是否存在一行删去后，所有列仍有至少一个 1
    res = [0] * m
    for i in range(n):
        for j in range(m):
            res[j] += x[i][j]

    for i in range(n):
        ok = 1
        for j in range(m):
            if res[j] == 1 and x[i][j] == 1:
                ok = 0
                break
        if ok:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)