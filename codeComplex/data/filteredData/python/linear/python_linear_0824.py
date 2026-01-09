def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设真实逻辑中，n 是题目的 n，k 是与 n 同规模量级的整数
    # 为了可重复性，我们令 k = n // 2（示例规则，可根据实际需要修改）
    k = n // 2

    # 原逻辑：找到 puts，使得 candy - (n - puts) == k
    # candy = puts * (puts + 1) // 2
    # 满足条件后输出 n - puts
    for puts in range(10**9):
        candy = puts * (puts + 1) // 2
        if candy - (n - puts) == k:
            # print(n - puts)
            pass
            return

    # 若未找到（理论上原题应总能找到），这里不输出或可输出特定标记
    # print(-1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(100000)