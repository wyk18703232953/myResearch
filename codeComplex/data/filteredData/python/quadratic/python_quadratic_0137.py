import random

def main(n: int) -> int:
    # 生成测试数据：4 个 n×n 的 0/1 字符串网格，中间用空行分隔（逻辑只用到网格内容）
    pieces = []
    for i in range(4):
        grid = []
        for _ in range(n):
            # 随机生成一行，由 '0' 和 '1' 组成
            row = ''.join(random.choice('01') for _ in range(n))
            grid.append(row)
        pieces.append(grid)

    blacks = [0] * 4
    whites = [0] * 4

    # 按原逻辑计算每个棋盘的黑白格代价
    for i in range(4):
        grid = pieces[i]
        count = 0
        for j in range(n):
            for k in range(n):
                if (int(grid[j][k]) + j + k) % 2:
                    count += 1
        blacks[i] = count
        whites[i] = n * n - count

    ans = 4 * n * n
    for white1 in range(3):
        for white2 in range(white1 + 1, 4):
            for black1 in range(4):
                if black1 == white1 or black1 == white2:
                    continue
                for black2 in range(black1 + 1, 4):
                    if black2 == white1 or black2 == white2:
                        continue
                    ans = min(
                        ans,
                        whites[white1] + whites[white2] + blacks[black1] + blacks[black2],
                    )
    return ans

# 示例：需要时可以直接调用 main(n)，例如：
# result = main(5)
# print(result)