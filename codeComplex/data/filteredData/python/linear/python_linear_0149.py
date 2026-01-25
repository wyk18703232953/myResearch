def main(n):
    # 参数校正，保证 n 合法
    if n <= 0:
        return 0

    # 确定性生成 p 和数组 a
    p = n + 7  # 简单与 n 相关的确定性构造
    a = [(i * 3 + 1) % p for i in range(n)]

    t = 0
    k = 0
    for i in range(n):
        k += a[i]
    s = 0
    for i in range(0, n - 1):
        s += a[i]
        t = max(t, s % p + (k - s) % p)
    print(t)
    return t


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次调用
    main(10)