def main(n):
    MOD = 1000000007
    MOD2 = 1000000006

    # 确定性构造 x, k，随 n 增大而增大
    x = n * n + 1
    k = 2 * n + 3

    if x == 0:
        # print(0)
        pass
        return 0

    def helper(num):
        if num == 0:
            return 1
        p = 1
        ret = 2
        while num >= 2 * p:
            p *= 2
            ret = (ret ** 2) % MOD
        return ret * helper(num - p)

    x = x % MOD
    k = k % MOD2
    a = helper(k)
    # print((2 * a * x - a + 1) % MOD)
    pass
    return 0


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次调用
    main(10)