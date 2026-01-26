def main(n):
    # 映射：n 作为测试数据规模，表示接下来有 n 行 (f, t) 数据
    # 原程序第一行有两个输入：n 和 s，这里构造一个确定性的 s
    s = n  # 例如直接令 s = n
    ans = s
    for i in range(n):
        # 构造确定性 (f, t)：简单算术构造
        f = i
        t = i * 2
        ans = max(ans, t + f)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)