def main(n):
    # n 表示测试用例数量
    def process_pair(a, b):
        if a > b or a == b:
            c, d = a, b

        else:
            c, d = b, a
        e = [0]

        def fun(c, d):
            e[0] += c // d
            f = d
            d = c % d
            c = f
            if f > 0 and d > 0:
                fun(c, d)

        fun(c, d)
        return e[0]

    # 确定性生成 n 组 (a, b)
    results = []
    for i in range(1, n + 1):
        a = i + 1          # 保证 a > 0
        b = (i // 2) + 1   # 保证 b > 0 且有变化
        results.append(process_pair(a, b))

    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(5)