def main(n):
    """
    将原程序中由 input() 读入的 k 替换为由 n 生成的测试数据：
    这里约定：k = n
    可根据需要修改为其他生成方式。
    """
    k = n  # 生成测试数据：用 n 作为 k

    t = 0
    if k == 0:
        # print("Invalid input")
        pass
        return

    d = 0
    e = 0
    n = 5
    while True:
        u = 9 * n * (10 ** n) + 1 - (10 ** n) - 9 * k
        if u > 0:
            d += 1
            if e > 0:
                # 原代码中这里有 u = i，但留存原逻辑，只是 u 不再被 i 覆盖
                # u = i
                break
            n = n - 1
        elif u < 0:
            i = u
            e += 1
            if d > 0:
                n = n + 1
                break
            n = n + 1

        else:
            # print(9)
            pass
            return

    u = abs(u)
    u = u // 9
    m = u // n
    p = u % n
    if p == 0:
        q = 10 ** (n - 1) + m - 1
        o = q % 10

    else:
        q = 10 ** (n - 1) + m
        o = (q // (10 ** (n - p))) % 10
    # print(o)
    pass


# 示例：调用 main(10)
if __name__ == "__main__":
    main(10)