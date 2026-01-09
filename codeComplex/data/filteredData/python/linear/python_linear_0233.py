def main(n):
    # 生成确定性输入：
    # 原程序结构：
    # n: 字符串长度
    # s: 由 'x' 和 'y' 组成的字符串
    # 这里用简单周期模式生成字符串，含有足够多的 'x' 段，便于算法运行
    from itertools import groupby

    if n <= 0:
        # print(0)
        pass
        return

    # 构造长度为 n 的字符串，模式为 'xxxy' 重复
    base_pattern = ['x', 'x', 'x', 'y']
    s_list = [base_pattern[i % 4] for i in range(n)]
    s = "".join(s_list)

    x = [len(list(group)) for key, group in groupby(s) if key == "x"]
    ans = sum(max(0, l - 3 + 1) for l in x)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值做规模化实验
    main(10)