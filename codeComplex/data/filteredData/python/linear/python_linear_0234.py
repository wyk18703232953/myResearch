def main(n: int):
    """
    根据规模 n 生成一个长度为 n 的测试字符串 x，
    然后执行原始逻辑：
    统计需要删除的 'x' 的个数，使得不存在长度 >= 3 的连续 'x'。
    """

    # 3. 根据 n 生成测试数据（示例：周期性地生成包含 'x' 和 'y' 的字符串）
    # 你可以根据需要修改生成策略
    pattern = "xxxy"
    x = (pattern * (n // len(pattern) + 1))[:n]

    # 原逻辑开始
    c = 0
    ans = 0
    for ch in x:
        if ch == 'x':
            c += 1

        else:
            ans += max(0, c - 2)
            c = 0
    ans += max(0, c - 2)

    # 输出结果
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)