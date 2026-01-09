def main(n):
    # 解释原程序输入结构：
    # 第一行：n, s
    # 接下来 n 行：f, t
    #
    # 为了可规模化与确定性：
    # - n 仍然表示后续行数
    # - s 由 n 确定性生成，例如 s = n
    # - 每一行 (f, t) 由 i 和 n 确定性生成

    # 生成 s
    s = n

    # 初始化最大值
    maxi = s

    # 生成 n 组 (f, t)，保持确定性
    # 例如：
    # f_i = i
    # t_i = n - i
    # 这样 f_i + t_i = n，对所有 i 相同，便于保持逻辑简单和可控
    for i in range(n):
        f = i
        t = n - i
        maxi = max(maxi, f + t)

    # print(maxi)
    pass
if __name__ == "__main__":
    main(10)