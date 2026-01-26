def main(n):
    # 原程序结构：
    # n: 棋盘规模
    # x, y: 坐标
    # 这里将输入规模 n 直接作为棋盘规模
    # x, y 由 n 确定性生成
    x = n // 3 + 1
    if x > n:
        x = n
    y = (2 * n) // 3 + 1
    if y > n:
        y = n

    d0 = max(x - 1, y - 1)
    d1 = max(n - x, n - y)
    result = 'White' if d0 <= d1 else 'Black'
    # print(result)
    pass
if __name__ == "__main__":
    main(10)