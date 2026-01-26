def main(n):
    # 解释输入结构：
    # 原程序输入：
    # n, a, b, c, T
    # t1 t2 ... tn
    #
    # 将实验规模映射为：
    #   n -> ts 的长度
    #
    # 为了保持算法结构，构造确定性数据：
    #   a = 1
    #   b = 2
    #   c = 3
    #   T = n
    #   ts[i] = i % (n + 1) （保证 ts 中元素不超过 T）
    #
    # 这样随着 n 增大，循环规模也随之增大，便于时间复杂度实验。

    if n <= 0:
        # print(0)
        pass
        return

    a = 1
    b = 2
    c = 3
    T = n

    ts = [i % (n + 1) for i in range(n)]
    ts.sort()

    ans = 0
    for t in ts:
        temp = -10**18
        for u in range(t, T + 1):
            temp = max(temp, c * (u - t) + a - b * (u - t))
        ans += temp
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可以修改 n 以做不同规模的时间复杂度实验
    main(10)