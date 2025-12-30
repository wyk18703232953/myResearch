def main(n):
    """
    n: 控制测试数据规模，1~若干
    这里简单根据 n 生成 3 张牌 (类似题目中 t1, t2, t3)：
      - n % 5 控制点数
      - n % 3 控制花色
    """
    # 点数和花色的简单生成（1~9）
    ranks = [str((n + i) % 9 + 1) for i in range(3)]
    suits = ['m', 'p', 's']
    cards = [ranks[i] + suits[(n + i) % 3] for i in range(3)]

    t1, t2, t3 = cards

    if t1 == t2 and t2 == t3:
        print(0)
        return

    ts = [(int(t[0]), t[1]) for t in [t1, t2, t3]]
    ts.sort()
    ns = [t[0] for t in ts]
    ss = [t[1] for t in ts]

    if ns[0] + 1 == ns[1] and ns[0] + 2 == ns[2] and ss[0] == ss[1] and ss[1] == ss[2]:
        print(0)
        return
    if ns[0] + 2 >= ns[1] and ss[1] == ss[0]:
        print(1)
        return
    if ns[1] + 2 >= ns[2] and ss[1] == ss[2]:
        print(1)
        return
    if ns[0] + 2 >= ns[2] and ss[0] == ss[2]:
        print(1)
        return
    if ts[0] == ts[1] or ts[1] == ts[2] or ts[2] == ts[0]:
        print(1)
        return

    print(2)


if __name__ == "__main__":
    # 示例：以 n=1 运行
    main(1)