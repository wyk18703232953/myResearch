def main(n):
    # n 表示数组长度
    if n <= 0:
        print(-1)
        return

    # 确定性生成两行输入数据
    # 第一行：p 序列，从 1 到 n
    p_list = [i + 1 for i in range(n)]
    # 第二行：c 序列，一些简单确定性权值
    c_list = [i % 7 + 1 for i in range(n)]

    acc = {0: 0}
    for p, c in zip(p_list, c_list):
        adds = []
        for b, u in acc.items():
            a = p
            bb = b
            while bb:
                a, bb = bb, a % bb
            adds.append((a, u + c))
        for a, u in adds:
            acc[a] = min(u, acc.get(a, 1000000000))
    print(acc.get(1, -1))


if __name__ == "__main__":
    main(10)