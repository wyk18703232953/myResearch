def main(n):
    # 映射：n -> 原程序中的 n, m
    # 为了可规模化，令原始 n = n，m = n（可以根据需要调整）
    orig_n = n
    m = n

    # 确定性地生成 m 对 (a, b)
    # 虽然原程序并未使用 l, r，但保留其结构
    l = []
    r = []
    for i in range(m):
        a = i + 1
        b = (i + 1) * 2
        l.append(a)
        r.append(b)

    # 保持原程序的输出逻辑：输出长度为 n 的 0/1 序列
    for i in range(orig_n):
        if i % 2 == 0:
            # print(0, end='')
            pass

        else:
            # print(1, end='')
            pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小
    main(10)