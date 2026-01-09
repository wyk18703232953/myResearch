def main(n):
    a = [0 for _ in range(256)]
    # 设计输入规模映射：
    # k: 窗口大小，取 1 到 10 之间，与 n 相关但有上界
    # 序列长度 m: 与 n 相关，并且元素值在 [0, 255] 内
    k = max(1, min(10, n))
    m = min(n, 256)

    # 生成确定性的序列 c_list，元素在 0..255
    # 使用简单算术构造：c_i = (i * 37 + n) % 256
    c_list = [(i * 37 + n) % 256 for i in range(m)]

    # 原程序逻辑
    output = []
    for c in c_list:
        if a[c] != 0:
            output.append(str(a[c] - 1))

        else:
            for x in range(c, c - k, -1):
                if a[x] == 0:
                    i = x

                else:
                    if c - a[x] + 1 < k:
                        i = a[x] - 1
                    break
                if x == 0:
                    break
            for x in range(int(i), c + 1):
                a[x] = i + 1
            output.append(str(i))

    # print(" ".join(output))
    pass
if __name__ == "__main__":
    main(100)