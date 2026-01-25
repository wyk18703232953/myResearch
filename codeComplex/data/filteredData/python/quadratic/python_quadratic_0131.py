def main(n):
    # 将原来的 (n, m) 输入结构映射为：
    # n: 元素范围 [1, n]
    # m: 列表长度，为 n 的平方，保证规模可控且与 n 相关
    m = n * n

    q = {i: 0 for i in range(1, n + 1)}

    # 生成长度为 m 的序列，元素在 1..n 之间，采用确定性公式
    # 对应原程序第二行输入的 m 个整数
    sequence = [(i % n) + 1 for i in range(m)]

    for x in sequence:
        q[x] += 1

    print(min(q.values()))


if __name__ == "__main__":
    main(10)