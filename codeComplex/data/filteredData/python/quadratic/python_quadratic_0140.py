import random

def main(n: int) -> int:
    # 生成测试数据：4 个 n×n 的 0/1 矩阵
    a = []
    for _ in range(4):
        grid = []
        for _ in range(n):
            row = [random.randint(0, 1) for _ in range(n)]
            grid.append(row)
        a.append(grid)

    # 原逻辑开始
    b = []
    for i in range(4):
        b.append([])
        for j in range(2):
            c = 0
            for y in range(n):
                for x in range(n):
                    if j == 1:
                        z = (x + y) % 2
                    else:
                        z = 1 - (x + y) % 2
                    c += a[i][y][x] != z
            b[-1].append(c)

    ans = float("inf")
    for i in (3, 5, 6, 9, 10, 12):
        ans = min(
            ans,
            b[0][i & 1]
            + b[1][(i >> 1) & 1]
            + b[2][(i >> 2) & 1]
            + b[3][(i >> 3) & 1],
        )
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)