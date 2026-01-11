def main(n):
    # 映射：n 作为数组长度，m 设为 n 的 2 倍，保持原逻辑中的 m 与 n 的关系可扩展
    if n <= 0:
        return

    m = 2 * n

    # 生成确定性的输入数组 lst，长度为 n
    # 使用简单算术构造，让数组中存在重复元素，便于统计频次
    # 模式：lst[i] = i % max(1, n // 3)
    # 保证当 n 较小时也有合理分布
    base = max(1, n // 3)
    lst = [i % base for i in range(n)]

    res = list(dict.fromkeys(lst))
    c = []
    for i in range(len(res)):
        c.append(lst.count(res[i]))

    if m < n:
        # print(0)
        pass
    elif m == n:
        # print(1)
        pass

    else:
        m1 = 1
        j = 2
        f = 0
        while True:
            c1 = 0
            for i in range(len(c)):
                c1 += c[i] // j
            if c1 >= n:
                m1 = j
                j += 1

            else:
                f = 1
            if f == 1:
                # print(m1)
                pass
                break


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模做时间复杂度实验
    main(10)