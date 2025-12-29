def main(n: int):
    # 根据规模 n 生成测试数据：
    # 令 l 和 r 为 [0, 2^n - 1] 区间两端
    # 为避免过大，限制 n 不超过 60
    n = min(max(n, 1), 60)
    l = 0
    r = (1 << n) - 1

    if l == r:
        print(0)
    else:
        rs = ""
        rr = r
        while rr:
            rs += '1' if rr % 2 else '0'
            rr //= 2
        for _ in range(len(rs), 65):
            rs += '0'

        ls = ""
        ll = l
        while ll:
            ls += '1' if ll % 2 else '0'
            ll //= 2
        for _ in range(len(ls), 65):
            ls += '0'

        pos = -1
        for i in range(64, -1, -1):
            if rs[i] == '1' and ls[i] == '0':
                pos = i
                break

        ans = 2 ** (pos + 1) - 1
        print(ans)


if __name__ == '__main__':
    # 示例：以 n = 10 运行
    main(10)