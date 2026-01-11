def main(n):
    # 根据 n 构造确定性的 m 和 n 对应的条目数量
    # 这里将 n 解释为原程序中的 n（行数），m 随 n 缩放
    m = n * 5  # 可调的线性规模映射

    l = []
    s1 = 0
    s2 = 0

    # 生成确定性的 (a, b) 对
    # 使得数据既有 a > b 也有 a < b 的情况，避免退化
    for i in range(1, n + 1):
        a = 3 * i + (i % 4)   # 简单确定性构造
        b = 2 * i + (i % 3)
        s1 += a
        s2 += b
        l.append(a - b)

    if s1 <= m:
        # print(0)
        pass
    elif s2 > m:
        # print(-1)
        pass

    else:
        r = 0
        l.sort(reverse=True)
        for diff in l:
            r += 1
            s1 -= diff
            if s1 <= m:
                # print(r)
                pass
                break


if __name__ == "__main__":
    # 示例：可根据需要调整 n 进行规模化实验
    main(10)