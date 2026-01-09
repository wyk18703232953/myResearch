def main(n):
    # 映射含义：
    # 原程序中：n = 序列长度, m = 区间数量
    # 这里设 m = n，用确定性方式生成 m 对区间 (a, b)
    m = n

    l = []
    r = []
    for i in range(m):
        a = (i % n) + 1 if n > 0 else 1
        b = ((i * 2) % n) + 1 if n > 0 else 1
        if a > b:
            a, b = b, a
        l.append(a)
        r.append(b)

    # 保持原核心输出逻辑
    for i in range(n):
        if i % 2 == 0:
            # print(0, end='')
            pass

        else:
            # print(1, end='')
            pass
if __name__ == "__main__":
    main(10)