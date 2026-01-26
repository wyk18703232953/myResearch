def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设定：
    # l = n, r = 2n + 1（保证 r >= l 且有一定差异）
    l = n
    r = 2 * n + 1

    if l == r:
        # print(0)
        pass

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
        # print(ans)
        pass
if __name__ == '__main__':
    # 示例：调用 main(10)，可按需修改或在外部调用 main
    main(10)