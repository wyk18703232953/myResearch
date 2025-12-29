def main(n):
    # 这里将原先的输入 s 作为规模 n 的函数，例如设 s = n。
    # 如果在你的应用中 s 的含义不同，可以按需要修改这一行。
    s = n

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

    # 返回结果而非直接打印，便于在外部调用和测试
    return max(n - r + 1, 0)


if __name__ == "__main__":
    # 示例：调用 main(100) 并打印结果
    print(main(100))