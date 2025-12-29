MOD = 10**9 + 7

def main(n: int):
    """
    n 为规模参数，用来生成测试数据 (l, r)。
    这里示例使用固定规则：
      - 若 n 为偶数：l = n, r = 2*n
      - 若 n 为奇数：l = 1, r = n
    可根据需要自行调整生成方式。
    """
    if n <= 0:
        # 给一个默认合法区间
        l, r = 0, 0
    else:
        if n % 2 == 0:
            l, r = n, 2 * n
        else:
            l, r = 1, n

    if l - r == 0:
        print(0)
    else:
        a = list(format(l, '064b'))
        b = list(format(r, '064b'))
        i = 0
        ll = l
        rr = r
        while i < 64 and a[i] == b[i]:
            i += 1
        for i in range(i, 64):
            if a[i] == '0' and b[i] == '0':
                k = l ^ (2 ** (64 - i - 1))
                if k <= rr:
                    l = k
                    a[i] = '1'
            elif a[i] == '1' and b[i] == '1':
                k = r - (2 ** (64 - i - 1))
                if k >= ll:
                    b[i] = '0'
                    r = k
        print(l ^ r)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 进行简单测试
    main(10)