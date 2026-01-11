def main(n):
    d = {}
    # 使用 n 作为第一部分输入规模
    # 构造 n 对 (a, b)
    for i in range(n):
        a = i
        b = (i * 2 + 1)  # 确定性生成
        d[a] = b

    s = 0
    # 第二部分输入规模设为 n
    m = n
    for i in range(m):
        x = i // 2  # 可能与已有 key 冲突，也可能是新 key
        y = i * 3 + 1
        if x in d:
            d[x] = max(d[x], y)

        else:
            d[x] = y

    for key in d:
        s += d[key]
    # print(s)
    pass
if __name__ == "__main__":
    main(10)