def main(n):
    # 根据规模 n 生成 s，这里示例取 s = n // 2，可按需要调整生成规则
    s = n // 2

    r = 10**18 + 1
    l = 0

    def f(m):
        res = 0
        while m > 0:
            res += m % 10
            m //= 10
        return res

    while r - l > 1:
        mid = (r + l) // 2
        if mid - f(mid) >= s:
            r = mid
        else:
            l = mid

    print(max(n - r + 1, 0))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10**6)